import streamlit as st


def run_home() :
    st.text('')

    st.subheader('과거 데이터를 기반으로 분석하여 영화의 수익 예측을 진행합니다.')
    st.info('데이터 출처 : top-500-movies.csv (Kaggle), new_movie.csv (top-500-movies.csv 컬럼 일부 수정)')
    st.text('')

    st.text('EDA 탭에서는 과거 데이터 분석을 실시하며, ML 탭에서는 신규 데이터 예측을 실시합니다.')
    st.subheader('')
    
    st.image('image/deadpool.jpg', use_container_width = True)