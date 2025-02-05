import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time

# 스타일 적용
st.markdown(
    """
    <style>
        .big-font { font-size:30px !important; font-weight: bold; text-align: center; }
        .sub-header { font-size:22px !important; font-weight: bold; }
        .info-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
        .button { font-size:18px; font-weight: bold; color: white; background-color: #ff4b4b; padding: 10px 20px; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

def run_ml():
    st.markdown('<p class="big-font">🎬 ML 기반 영화 박스오피스 예측</p>', unsafe_allow_html=True)
    st.markdown('<p class="info-box">영화의 기본 정보를 입력하면 예상 박스오피스 수익을 예측해드립니다.</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="sub-header">📌 영화 정보 입력</p>', unsafe_allow_html=True)

    menu_rating = ['전체 관람가', '12세 이상 관람가', '15세 이상 관람가', '청소년 관람 불가']
    menu_genre = ['액션', '어드벤처', '블랙 코미디', '코미디', '드라마', '호러', '뮤지컬', '로맨틱 코미디', '스릴러/서스펜스', '서부극']

    title = st.text_input('🎥 영화 제목')
    
    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input('📅 개봉 연도', min_value=1900, max_value=2040, value=2025)
        runtime = st.number_input('⏳ 상영 시간 (분)', min_value=0, value=120)
    with col2:
        mpaa = st.selectbox('🔖 상영 등급', menu_rating)
        genre = st.selectbox('🎭 장르', menu_genre)

    cost = st.number_input('💰 제작 비용 ($)', step=1000000, value=100000000)
    opening = st.number_input('🎟 개봉 주 수익 ($)', step=1000000, value=100000000)

    classifier = joblib.load('model/classifier.pkl')

    mpaa_dict = {'전체 관람가': 0, '12세 이상 관람가': 1, '15세 이상 관람가': 2, '청소년 관람 불가': 3}
    genre_dict = {
        '액션': 0, '어드벤처': 1, '블랙 코미디': 2, '코미디': 3, '드라마': 4,
        '호러': 5, '뮤지컬': 6, '로맨틱 코미디': 7, '스릴러/서스펜스': 8, '서부극': 9
    }

    data_classify = np.array([cost, mpaa_dict[mpaa], genre_dict[genre], runtime, year]).reshape(1, 5)
    new_data_classify = pd.DataFrame(data_classify)

    if st.button('📊 수익 예측', disabled=not title):
        st.markdown('<p class="sub-header">🔍 예측 결과</p>', unsafe_allow_html=True)

        pred_group = classifier.predict(new_data_classify)

        label_group = {0: '미들 마켓', 1: '메가 블록버스터', 2: '블록버스터'}[pred_group[0]]
        st.success(f'🎬 영화 **"{title}"** 은(는) **{label_group}** 영화군요!')
        
        with st.spinner('⏳ 수익 예측을 실시하는 중...'):
            time.sleep(2)

            regressor = joblib.load('model/regressor.pkl')
            data_predict = np.array([cost, opening, mpaa_dict[mpaa], genre_dict[genre], runtime, year]).reshape(1, 6)
            pred_profit = regressor.predict(data_predict)[0][0]
            pred_dom_profit = int(pred_profit.round())

            if pred_dom_profit >= 0:
                pred_dom_profit = format(pred_dom_profit, ',')
                st.subheader(f'📈 예상 북미 박스오피스 수익: **{pred_dom_profit} 달러**')

                time.sleep(1)

                # wrld_dom_ratio : domestic gross 대비 worldwide gross의 일반적인 비율
                # max값이 과도하게 큰 관계로 mean값 대신 median값을 wrld_dom_ratio로 설정 (세부 사항은 ratio_movie.ipynb 참고)
                wrld_dom_ratio = 2.7
                pred_wrld_profit = int((pred_profit * wrld_dom_ratio).round())
                pred_wrld_profit = format(pred_wrld_profit, ',')
                st.subheader(f'🌍 예상 전세계 박스오피스 수익: **{pred_wrld_profit} 달러**')
            else:
                st.error('❌ 예측이 불가능한 데이터입니다.')