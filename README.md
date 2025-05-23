# 🎬 영화 수익 예측 웹앱

### 영화의 수익을 예측하는 인공지능 웹 애플리케이션

---

## 📌 앱 개요
이 애플리케이션은 영화 데이터를 분석하여 특정 영화의 유형을 분류하고, 북미 박스오피스 수익을 예측한 후 이를 바탕으로 전 세계 박스오피스 수익까지 추정하는 기능을 제공합니다. 사용자는 영화의 다양한 특성을 입력하여 예상 수익을 확인할 수 있습니다. <br><br>
애플리케이션 링크 : [Streamlit Application](https://movie-profit-app-codekookiz.streamlit.app/)

---

## 📀 사용 기술 및 라이브러리

### 💻 프로그래밍 언어: Python

|          분야          |         라이브러리         |
|-----------------------|-------------------------|
|      웹 프레임워크       |         Streamlit       |
|       데이터 처리        |     Pandas<br>Numpy     |
|  머신러닝 모델 학습 및 평가 | Scikit-learn<br>XGBoost |
| 데이터 시각화 및 그래프 출력 |  Matplotlib<br>Seaborn  |
|    모델 저장 및 로드      |         Joblib          |

---

## 🍿 주요 기능

### 🔍 1. 영화 유형 분석
- 사용자가 입력한 영화 정보(제작비용, 개봉 연도, 장르 등)를 바탕으로 K-Means 클러스터링을 활용하여 유형을 분류합니다.
- 최적의 클러스터 개수를 자동으로 탐색하여 최적화된 결과를 제공합니다.

### 💰 2. 북미 수익 예측
- LinearRegression 모델을 사용하여 북미 박스오피스 수익을 예측합니다.
- 입력된 영화 정보에 따라 실시간으로 수익을 계산합니다.

### 🌍 3. 전 세계 수익 예측
- 북미 수익 대비 전 세계 수익 비율의 중앙값(median)을 활용하여 전 세계 수익을 추정합니다.
- 비율 계산을 통해 보다 현실적인 전 세계 수익을 제공합니다.

---

## 🚀 Streamlit 배포

1. 로컬 환경에서 앱 테스트 후 `requirements.txt`를 생성하여 필요한 라이브러리 목록을 관리합니다.
2. GitHub에 애플리케이션를 업로드합니다.
3. Streamlit Share를 활용하여 외부에서 접속 가능하도록 배포합니다.

---

## 📂 애플리케이션 구조

```
📁 movie-profit-app/
│── 📄 app.py                      # 애플리케이션 메인 파일 (Streamlit)
|── 📂 data/
│   │── 📄 new_movie.csv           # 클러스터링 이후 데이터
│   │── 📄 result.csv              # 예측 결과 데이터
│   │── 📄 top-500-movies.csv      # 원본 데이터
|── 📂 image/
│   │── 📄 main_home.png           # 홈 화면 메인 이미지
│   │── 📄 main_sidebar.png        # 사이드바 메인 이미지
|── 📂 jupyter_notebook/
│   │── 📄 classify_movie.ipynb        # 신규 데이터 분류 모델 파일 생성한 주피터 노트북
│   │── 📄 cluster_movie.ipynb         # 기존 데이터 분류한 csv 파일 생성한 주피터 노트북
│   │── 📄 predict_movie.ipynb         # 신규 데이터 예측 모델 생성한 주피터 노트북
│   │── 📄 ratio_movie.ipynb           # 수익 비율 계산한 주피터 노트북
│   │── 📄 result_movie.ipynb          # 예측 결과 저장하는 csv 파일 생성한 주피터 노트북
│── 📂 model/
│   │── 📄 classifier.pkl          # 분류 모델
│   │── 📄 regressor.pkl           # 예측 모델
|── 📂 ui/
│   │── 📄 eda.py                  # 탐색적 데이터 분석 (EDA) 탭
│   │── 📄 home.py                 # 홈 화면 탭
│   │── 📄 info.py                 # 앱 정보 탭
│   │── 📄 ml.py                   # 머신 러닝 (ML) 탭
│   │── 📄 stat.py                 # 통계 데이터 탭
│── 📄 README.md                   # 애플리케이션 설명 파일
```

---

## 🏗 개발 프로세스

1. **데이터 수집 및 전처리**
   - Kaggle에서 `top-500-movies.csv` 데이터를 다운로드하여 활용.
   - NaN 값은 평균값으로 대체하거나 삭제.
   - 필요한 정보(제작비용, 개봉 주말 수익, 상영 등급, 장르, 상영관 수, 상영 시간, 개봉 연도)만 추출.

2. **영화 유형 분류**
   - LabelEncoder를 사용하여 문자열 데이터를 변환.
   - K-Means 클러스터링 수행 (최대 10개 클러스터 설정).
   - 엘보우 메소드를 활용하여 최적의 클러스터 개수를 자동 탐색.
   - 도출된 클러스터 정보를 원본 데이터에 추가하여 `new_movie.csv`로 저장.

3. **영화 수익 예측**
   - LinearRegression을 포함한 3가지 모델 성능 비교 (LinearRegression, RandomForestRegressor, XGBRegressor).
   - 최종적으로 LinearRegression 모델을 선택 (정확도 73%).

4. **전 세계 수익 예측**
   - 북미 수익 대비 전 세계 수익의 일반적인 비율 분석.
   - 평균값이 너무 큰 영향을 주므로, 중앙값(median)으로 설정하여 보다 신뢰할 수 있는 예측 모델 구축.

---

## 📬 개발자 연락처
📧 Email: codekookiz@gmail.com
