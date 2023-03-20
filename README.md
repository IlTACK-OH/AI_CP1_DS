❗️ 아직 미완성된 REPO와 README입니다.

# <div align="center">AI_CP1_DS: 과적차량 탐지🚛</div>
### 프로젝트 목표
주어진 도로 이미지 또는 영상 데이터에서 과적차량과 정상차량을 탐지해내는 것.
### 사용 Stacks


# Conda 및 Python 환경
- Conda version: 23.1.0
- Python version: 3.9.16
# 사용법
```
git clone https://github.com/IlTACK-OH/AI_CP1_DS.git
cd AI_CP1_DS
pip install -r requirements.txt
python detection.py --onnx_path [가중치 파일 경로] --source [데이터 파일 경로] --output [결과 저장파일 경로] --conf [confidence threshold]
```
- onnx_path: onnx형식의 가중치 파일이 저장된 파일 경로를 입력합니다. (default: ./models/test.onnx)
- source: 객체 탐지를 진행하고자 하는 파일 경로입니다. (default: ./data)
- output: 탐지 결과 파일을 저장할 파일 경로입니다. (default: ./results)
- conf: confidence threshold입니다. (default: 0.25, float 타입)
