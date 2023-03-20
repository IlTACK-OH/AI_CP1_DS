❗️ 가상의 기업 M기업에서 과적차량 단속 서비스 개발이라는 상황을 가정합니다.

---

# <div align="center">AI_CP1_DS: 과적차량 탐지🚛</div>
### 프로젝트 목표
주어진 도로 이미지 또는 영상 데이터에서 불법차량(적재불량: 길이과적, 높이과적)과 정상차량을 탐지해내는 것.
### 사용 Stacks
 <div style="margin: 0 auto; text-align: center;" align= "center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/YOLOv5-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black"><img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white"></div>

## 프로젝트 개요
 <div style="margin: 0 auto; text-align: center;" align= "center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbs5dn8%2FbtrGApdFKqy%2FZQCk39KOCdXr09YfVxsglk%2Fimg.jpg"></div>
과적차량의 통행은 고속도로 포장 면에 거북등 균열, 블로우업 현상, 소성변형, 국부파손들을 초래하여 수명을 단축한다. 또한 교량의 내하력을 떨어뜨리고 피로도를 가중해 교량의 파손을 가져온다.<br><br>
그리고 저속주행으로 인하여 교통소통에 지장을 주어 고속도로의 교통용량과 기능을 저하하며, 타이어 파손, 전후방 시야 가림 등 잦은 고장의 원인이 되어 교통사고를 유발하기도 한다.<br><br>
그 중 길이과적과 높이과적의 경우 도로법 시행령 기준 차량의 폭이 2.5m, 높이가 4.0m, 길이가 16.7m를 초과하는 경우 과적차량으로 분류한다.<br><Br>
이런 과적차량 중 영상 또는 이미지로 단속 가능한 길이, 높이 과적차량을 탐지하는 단속 서비스를 개발하여 보다 안전한 도로환경 구성하는 것을 목표로 한다.
 
 ## 패키지의 디렉토리 구조
 ```
 AI_CP1_DS
├── data
│   └── (image and video sample)
├── moels
│   └── test.onnx
├── results
│   └── (results of image and video sample)
├── utils
│   └── __init__.py
│   └── image.py
│   └── video.py
├── detection.py
└── requirements.txt
 ```
-  `.gitignore`과 `README.md`는 따로 표시하지 않음.

### ✏ data
모델 추론의 입력값으로 사용될 영상 및 이미지 파일들의 샘플이 들어있습니다.<br>
detection.py를 실행할 때 `source`의 default 경로로 설정되어 있습니다.
### ✏ models
추론에 사용될 사전 학습된 모델의 가중치 파일(.onnx)이 저장되어 있습니다.<br>
이 폴더 역시 마찬가지로 detection.py를 실행할 때 `onnx_path`의 default 경로로 설정되어 있습니다.
### ✏ results
detection.py에 의하여 생성된 영상이 저장되는 폴더입니다.<br>
이 폴더 역시 마찬가지로 detection.py를 실행할 때 `output`의 default 경로로 설정되어 있습니다.
### ✏ utils
models 내 모델을 통하여 이미지 또는 영상 내 객체를 탐지하는 Object deteciton을 진행하고 결과를 .mp4형식으로 생성하는 image모듈과 video모듈이 저장되어 있습니다.
- **__init.py**<br>
 해당 파일은 해당 파일을 포함한 폴더가 패키지의 일부임을 알려주는 역할을 합니다.
- **image.py**<br>
 해당 파일은 주어진 데이터가 이미지일 경우 models 내 모델을 통하여 이미지 내 객체 탐지를 진행하는 모듈입니다.
- **video.py**<br>
 해당 파일은 주어진 데이터가 영상일 경우 models 내 모델을 통하여 이미지 내 객체 탐지를 진행하는 모듈입니다.
### ✏ detection.py
 해당 파일은 utils의 모듈과 models 내 저장된 모델을 이용하여 객체 탐지를 진행하는 파일이다.<br>터미널에서 실행할 수 있도록 구성되어 있습니다.
### ✏ requirements.txt
 프로젝트에 필요한 패키지 파일들이 필요한지 작성되어 있습니다.

# Conda 및 Python 환경
- Conda version: 23.1.0
- Python version: 3.9.16

# 사용법
**❗ 반드시 안내사항까지 확인하신 후 사용하길 강력히 권고드립니다.**<br>
터미널에서 다음과 같이 입력해 주세요.
```
git clone https://github.com/IlTACK-OH/AI_CP1_DS.git
cd AI_CP1_DS
pip install -r requirements.txt
python detection.py --onnx_path [가중치 파일 경로] --source [데이터 파일 경로] --output [결과 저장파일 경로] --conf [confidence threshold]
```
사용의 편의를 위하여 모델의 가중치와 데이터 파일의 경로 그리고 저장될 경로, confidence score까지 사용자가 조작할 수 있게 구성하였습니다.<br>
 그리고 각 인수가 의미하는 바는 다음과 같습니다.
- onnx_path: onnx형식의 가중치 파일이 저장된 파일 경로를 입력합니다. (default: ./models/test.onnx)
- source: 객체 탐지를 진행하고자 하는 데이터 폴더의 경로를 입력합니다. (default: ./data) 
- output: 탐지 결과 파일을 저장할 폴더 경로입니다. (default: ./results)
- conf:<br> confidence threshold입니다. 이는 Box가 객체(어떤 Class인지는 모르지만 객체가 있는지 없는지)가 있는지에 대한 가능성과 정확도를 판단하는 기준이 됩니다. (default: 0.25, float 타입)

 이때 각 인수를 입력하지 않고 다음과 같이 실행하면 모두 기본값으로 설정된 상태로 실행됩니다.
 ```
 python detection.py
 ```
### 사용예시
```
git clone https://github.com/IlTACK-OH/AI_CP1_DS.git
cd AI_CP1_DS
pip install -r requirements.txt
python detection.py --onnx_path C:\users\model\test.onnx  --source C:\users\data --output C:\users\results --conf 0.3
```
만일 위와 같이 입력했다면 다음을 의미합니다.
1. C:\users\model 경로에 있는 test.onnx라는 파일을 통하여 모델을 생성합니다.
2. C:\users\data 경로에 있는 파일들에 대해서 예측을 진행합니다. 이때 confidence threshold는 0.3입니다.
3. 예측의 결과는 C:\users\results에 저장됩니다.
<br>
굳이 가중치 파일이나, 데이터 폴더 등을 해당 프로젝트의 디렉토리 안으로 가져올 필요가 없으며, 저장될 경로 역시 지정만 정확히 한다면 원하는 곳에 저장할 수 있습니다.
 # ❗ 안내사항
 - `--source`의 인수는 반드시 `폴더`이어야 합니다. 그리고 그 폴더에는 오로지 예측 시 사용할 데이터만 들어있어야 합니다.
 - 파일 형식은 `.jpg`,`.png`, `.mp4`형식만 지원합니다.
 - 아직 openCV CUDA가속을 구현하지 못하여 CPU를 이용해 예측을 진행합니다. 따라서 영상의 길이가 긴 경우 시간이 오래 소요될 수 있습니다.
 - 만일 사용 중 오류가 발생하거나 사용 중 의문사항이 생기시면 `issues`탭을 통하여 글을 남겨주시길 바랍니다.
