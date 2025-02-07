import streamlit as st

def run_home():
    # 제목 스타일 개선
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            🎥 영화 수익 예측 개요
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.text('')

    # 설명 부분 스타일 개선
    st.markdown(
        """
        <p style="font-size: 18px; text-align: center;">
            🎬 과거 영화 데이터를 기반으로 <b>신규 영화의 예상 수익을 예측</b>하는 앱입니다!<br>
            데이터 분석과 머신러닝 모델을 활용하여 <b>흥행 가능성을 미리 확인해보세요.</b>
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 📌 데이터 출처 및 구성
    st.markdown("### 📌 **사용 데이터**")
    st.info(
        """
        - 🔹 **top-500-movies.csv** (출처: Kaggle)  
        - 🔹 **new_movie.csv** (일부 수정 및 추가 데이터 포함)  
        - 💡 영화의 제작비, 개봉 연도, 장르, 감독 등의 정보를 포함하며,  
          수익 예측을 위한 머신러닝 모델 학습에 활용됩니다.
        """
    )

    st.markdown("---")

    # 이미지 추가 (가운데 정렬)
    st.image("image/main_home.png", use_container_width=True)

    st.markdown("---")
    
    # 🎯 앱의 주요 기능 강조
    st.markdown("### 🎯 **이 앱으로 할 수 있는 일**")
    st.markdown(
        """
        - 📊 **과거 영화 데이터를 분석**하여 성공적인 영화의 특징을 탐색  
        - 🔍 **입력한 영화 정보**를 바탕으로 **예상 수익을 예측**  
        - 🎭 장르, 제작비, 감독, 개봉 연도 등의 요소가 **흥행에 미치는 영향 분석**  
        - 📈 **AI 기반 예측 모델**을 사용하여 흥행 여부를 예측  
        """
    )

    st.markdown("---")

    # ⚡ 기능 소개
    st.markdown("### ⚡ **이 앱의 주요 기능**")
    st.markdown(
        """
        - ✅ **과거 데이터 확인하기**: 기존 영화 데이터를 시각적으로 분석하고, 트렌드를 파악  
        - ✅ **영화 수익 예측하기**: 입력한 영화 정보를 바탕으로 AI 모델이 예상 수익을 예측  
        - ✅ **앱 정보**: 이 앱의 개요와 기능을 한눈에 확인  
        - ✅ **통계 데이터**: 관리자 전용 페이지로 추가적인 분석 기능 제공  
        """
    )

    st.markdown("---")

    # 📢 활용 예시 추가
    st.markdown("### 📢 **이렇게 활용할 수 있어요!**")
    st.markdown(
        """
        - 🎬 **영화 제작사** → 제작 전 예상 수익을 분석하여 투자 결정  
        - 🎞 **배급사** → 마케팅 전략을 세우기 전 예상 흥행 여부 판단  
        - 📺 **영화 애호가** → 과거 데이터를 통해 어떤 영화가 성공했는지 확인  
        """
    )

    st.markdown("---")