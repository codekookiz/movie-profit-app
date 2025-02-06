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

    st.markdown("---")

    # 설명 부분 스타일 개선
    st.markdown(
        """
        <p style="font-size: 18px; text-align: center;">
            과거 데이터를 분석하여 이를 토대로 새로운 영화의 예상 수익을 예측하는 앱입니다.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # 데이터 출처 강조
    st.info("📌 데이터 출처: **top-500-movies.csv** (Kaggle), **new_movie.csv** (일부 수정)")

    # EDA 및 ML 설명
    st.markdown(
        """
        ✅ **과거 데이터 확인하기**: 기존 영화 데이터 분석  
        ✅ **영화 수익 예측하기**: 신규 영화 데이터의 예상 수익 예측  
        ✅ **앱 정보**: 앱 기초 정보 제공  
        ✅ **통계 데이터**: 통계 데이터 제공 (관리자 전용)
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")


    # 이미지 추가 (가운데 정렬)
    st.image("image/main_home.png", use_container_width=True)

    st.markdown("---")