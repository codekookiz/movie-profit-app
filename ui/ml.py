import streamlit as st, joblib, numpy as np, pandas as pd
from sklearn.linear_model import LinearRegression


def run_ml() :
    st.subheader('')

    st.header('ML (머신러닝)')
    st.text('')

    st.info('영화의 기본 정보를 바탕으로 영화의 예상 박스오피스 수익을 알려드립니다.')
    st.subheader('')

    st.subheader('영화의 예상 박스오피스 수익 확인을 위해 하단 정보를 입력해주세요.')
    st.text('')

    menu_rating = ['전체 관람가', '12세 이상 관람가', '15세 이상 관람가', '청소년 관람 불가']
    menu_genre = ['액션', '어드벤처', '블랙 코미디', '코미디', '드라마', '호러', '뮤지컬', '로맨틱 코미디', '스릴러/서스펜스', '서부극']

    title = st.text_input('영화의 제목을 입력하세요.')
    st.text('')
    year = st.number_input('영화의 개봉 연도를 입력하세요.', min_value=1900, max_value=2040, value=1980)
    mpaa = st.selectbox('영화의 상영 등급을 선택하세요.', menu_rating)
    genre = st.selectbox('영화의 장르를 선택하세요.', menu_genre)
    runtime = st.number_input('영화의 상영 시간을 입력하세요.', min_value=0, value=60)
    cost = st.number_input('영화의 제작 비용을 입력하세요. ($)', step=1000, value=10000)
    opening = st.number_input('영화의 개봉 첫 주 수익을 입력하세요. ($)', step = 1000, value = 10000)
    st.subheader('')

    classifier = joblib.load('model/classifier.pkl')

    if mpaa == '전체 관람가' :
        new_mpaa = 0
    elif mpaa == '12세 이상 관람가' :
        new_mpaa = 1
    elif mpaa == '15세 이상 관람가' :
        new_mpaa = 2
    else :
        new_mpaa = 3

    if genre == '액션' :
        new_genre = 0
    elif genre == '어드벤처' :
        new_genre = 1
    elif genre == '블랙 코미디' :
        new_genre = 2
    elif genre == '코미디' :
        new_genre = 3
    elif genre == '드라마' :
        new_genre = 4
    elif genre == '호러' :
        new_genre = 5
    elif genre == '뮤지컬' :
        new_genre = 6
    elif genre == '로맨틱 코미디' :
        new_genre = 7
    elif genre == '스릴러/서스펜스' :
        new_genre = 8
    else :
        new_genre = 9

    data_classify = np.array([cost, new_mpaa, new_genre, runtime, year]).reshape(1, 5)
    new_data_classify = pd.DataFrame(data_classify)

    if st.button('수익 예측', disabled=not title) :
        st.text('')
        pred_group = classifier.predict(new_data_classify)

        if pred_group == 0 :
            label_group = '미들 마켓'
        elif pred_group == 1 :
            label_group = '메가 블록버스터'
        else :
            label_group = '블록버스터'

        st.subheader(f'영화 \'{title}\'은(는) {label_group} 영화군요!')
        st.text('')

        # 아래 글 표시하고 대기, 이후 결과 도출
        st.text('⏳ 수익 예측을 실시합니다.')
        st.text('')

        regressor = joblib.load('model/regressor.pkl')
        
        data_predict = np.array([cost, opening, new_mpaa, new_genre, runtime, year]).reshape(1, 6)
        pred_profit = regressor.predict(data_predict)[0][0]
        pred_dom_profit = int(pred_profit.round())

        if pred_dom_profit >= 0 :
            st.text('')
            pred_dom_profit = format(pred_dom_profit, ',')
            st.subheader(f'영화 \'{title}\'의 예상 북미 박스오피스 수익은 {pred_dom_profit} 달러입니다.')
            
            # wrld_dom_ratio : 국내 수익 대비 전세계 수익의 일반적 비율 -> max값이 과도하게 높기 때문에, mean값 대신 median값을 사용하기로 함
            # 세부사항은 ratio_movie.ipynb 참고
            wrld_dom_ratio = 2.7

            st.text('')
            pred_wrld_profit = int((pred_profit * wrld_dom_ratio).round())
            pred_wrld_profit = format(pred_wrld_profit, ',')
            st.subheader(f'영화 \'{title}\'의 예상 전세계 박스오피스 수익은 {pred_wrld_profit} 달러입니다.')
        else :
            st.subheader('예측이 불가능한 데이터입니다.')