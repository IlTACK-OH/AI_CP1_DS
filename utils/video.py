import os
import cv2
import numpy as np
import time

# Constants.
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45

# Text parameters.
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.8
THICKNESS = 2
 
# Colors.
BLUE   = (255,178,50)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)
WHITE = (255,255,255)

classes = ["illegal", "normal"]

def video_detect(net, video_path, output_path, conf):
    CONFIDENCE_THRESHOLD = conf
    
    # Load image or video using OpenCV
    if os.path.isfile(video_path):	# 해당 파일이 있는지 확인
        # 영상 객체(파일) 가져오기
        cap = cv2.VideoCapture(video_path)
    else:
        print("파일이 존재하지 않습니다.")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)
    
    start = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        img = frame.copy()
        
        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(frame, 1/255,  (INPUT_WIDTH, INPUT_HEIGHT), [0,0,0], 1, crop=False)
        
        # Sets the input to the network.
        net.setInput(blob)
    
        # Run the forward pass to get output of the output layers.
        outputs = net.forward(net.getUnconnectedOutLayersNames())
        
        
       # Lists to hold respective values while unwrapping.
        class_ids = []
        confidences = []
        boxes = []
        # Rows.
        rows = outputs[0].shape[1]
        image_height, image_width = img.shape[:2]
        # Resizing factor.
        x_factor = image_width / INPUT_WIDTH
        y_factor =  image_height / INPUT_HEIGHT
        # Iterate through detections.
        for r in range(rows):
            row = outputs[0][0][r]
            confidence = row[4]
            # Discard bad detections and continue.
            if confidence >= CONFIDENCE_THRESHOLD:
                    classes_scores = row[5:]
                    # Get the index of max class score.
                    class_id = np.argmax(classes_scores)
                    #  Continue if the class score is above threshold.
                    if (classes_scores[class_id] > SCORE_THRESHOLD):
                        confidences.append(confidence)
                        class_ids.append(class_id)
                        cx, cy, w, h = row[0], row[1], row[2], row[3]
                        left = int((cx - w/2) * x_factor)
                        top = int((cy - h/2) * y_factor)
                        width = int(w * x_factor)
                        height = int(h * y_factor)
                        box = np.array([left, top, width, height])
                        boxes.append(box)
        
        # Perform non maximum suppression to eliminate redundant, overlapping boxes with lower confidences.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        for i in indices:
                box = boxes[i]
                left = box[0]
                top = box[1]
                width = box[2]
                height = box[3]
                    
                # Class label.                      
                label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])
                
                # Get text size.
                text_size = cv2.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
                dim, baseline = text_size[0], text_size[1]
                
                # Draw bounding box.
                if classes[class_ids[i]] == "illegal":
                    cv2.rectangle(img, (left, top), (left + width, top + height), RED, 3*THICKNESS)
                    cv2.rectangle(img, (left,top), (left + dim[0], top + dim[1] + baseline), RED, cv2.FILLED)
                    cv2.putText(img, label, (left, top + dim[1]), FONT_FACE, FONT_SCALE, WHITE, THICKNESS, cv2.LINE_AA)
                elif classes[class_ids[i]] == "normal":
                    cv2.rectangle(img, (left, top), (left + width, top + height), BLUE, 3*THICKNESS)
                    cv2.rectangle(img, (left,top), (left + dim[0], top + dim[1] + baseline), BLUE, cv2.FILLED)
                    cv2.putText(img, label, (left, top + dim[1]), FONT_FACE, FONT_SCALE, WHITE, THICKNESS, cv2.LINE_AA)        
        # Write frame to output video
        out.write(img)
    # Release resources
    cap.release()
    out.release()