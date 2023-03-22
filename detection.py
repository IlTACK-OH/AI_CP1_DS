import argparse
import os
import sys
import time
from pathlib import Path


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

import cv2
from utils.video import video_detect
from utils.image import img_predict
def run(
    onnx_path = ROOT / 'models/test.onnx',
    source = ROOT / 'data',
    output = ROOT/ 'results',
    conf = 0.25
):
    start = time.time()
    
    # yolov5 모델 로드
    net = cv2.dnn.readNet(onnx_path)
    
    if cv2.cuda.getCudaEnabledDeviceCount():
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        print("Starts the object detection process. Use GPU")
    
    else:
        print("Starts the object detection process. Use CPU")
    num = len(os.listdir(source))
    n = 0
    print(f"\rNow complete: {n}/{num}",end =" ")
    
    for filename in os.listdir(source):   
        file_path = os.path.join(source, filename)
        output_path = os.path.join(output, filename)
        
        if file_path.endswith(".mp4"):
            video_detect(net = net, video_path = file_path, output_path=output_path, conf = conf)
        elif file_path.endswith(".jpg") or file_path.endswith(".png"):
            img_predict(net = net, image_path = file_path, output_path=output_path, conf = conf)
        else:
            print(f"\rSorry, we only support .png, .jpg, and .mp4 formats.Pleas check this file: {filename}")
    
        n += 1
        print(f"\rNow complete: {n}/{num}",end=" ")
    
    print(f"\n⭐️complete!!!⭐️ store in {output}")
    print(f"Wall time: {int((time.time()-start)//60)}min {(int(time.time()-start)%60)}s")

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--onnx_path', type=str, default=ROOT / 'models/test.onnx')
    parser.add_argument('--source', type=str, default= ROOT / 'data')
    parser.add_argument('--output', type=str, default= ROOT/ 'results')
    parser.add_argument('--conf', type=float, default= 0.25)
    args = parser.parse_args()
    return args

def main(args):
    run(**vars(args))
    
if __name__ == '__main__':
    args = parse_opt()
    main(args)