import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
import seaborn as sb
from pandas.api.types import is_integer_dtype, is_float_dtype, is_object_dtype
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans
from matplotlib import rc
from datetime import datetime, timedelta, timezone

from ui.eda import run_eda
from ui.home import run_home
from ui.info import run_info
from ui.ml import run_ml
from ui.stat import run_stat


def main():
    # 메인 타이틀 꾸미기
    st.markdown(
        """
        <h1 style='text-align: center; color: color: #4C82C2;'>
            🎬 영화 예상 수익 예측 앱
        </h1>
        <h2 style='text-align: center; 'color: #4C82C2;'>
            머신러닝 기반 예측
        </h2>
        """, unsafe_allow_html=True
    )

    st.markdown("""<hr style="border: none; height: 5px; background: #5B9BD5; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);">""",
                 unsafe_allow_html=True)
    
    # 사이드바 스타일 개선
    st.sidebar.image("image/main_sidebar.png", use_container_width=True)  
    
    # 📅 현재 날짜 & 시간 표시
    utc_now = datetime.now(timezone.utc)  # UTC 시간 가져오기
    kst_now = utc_now + timedelta(hours=9)  # KST 시간으로 변환

    # KST 시간 포맷에 맞게 출력
    now_str = kst_now.strftime("%Y-%m-%d %a %H:%M %p")
    st.sidebar.markdown(f"🕒 **현재 시간:** {now_str}")

    st.sidebar.markdown("---")

    df = pd.read_csv('data/new_movie.csv')
    count = len(df)
    prod = int((df['production_cost'].mean() / 1000000).round())
    prof = int((df['worldwide_gross'].mean() / 1000000).round())
    best = df.sort_values('worldwide_gross', ascending=False).iloc[0, :]['title']

    # 🎬 영화 데이터 요약 (예시 데이터)
    st.sidebar.markdown("### 📊 데이터 요약")
    col1, col2 = st.sidebar.columns(2)
    col1.metric("📈 총 영화 데이터", f"{count}개")
    col2.metric("💰 평균 제작비", f"${prod}M")

    col3, col4 = st.sidebar.columns(2)
    col3.metric("🎟 평균 수익", f"${prof}M")
    col4.metric("⭐️ 최고 흥행작", f"{best}")

    st.sidebar.markdown("---")

    # 📌 소셜 & 도움말 버튼 추가
    st.sidebar.markdown("### 🔗 유용한 링크")
    st.sidebar.link_button("🔍 GitHub Repository", "https://github.com/codekookiz/movie-profit-app")

    if st.sidebar.button("❓ 도움말 보기"):
        st.sidebar.info("이 앱은 영화 데이터를 분석하고 수익을 예측하는 머신러닝 기반 앱입니다.")

    st.sidebar.markdown("---")

    # 📌 크레딧
    st.sidebar.markdown("📌 Created by **CodeKookiz**  \n[🌍 Website](https://codekookiz.imweb.me)")

    # 탭 메뉴 생성
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 홈", "ℹ 앱 정보", "📊 과거 데이터 확인하기", "🎬 영화 수익 예측하기", "⚒️ 통계 데이터"])

    # 각 탭에 해당하는 기능 실행
    with tab1:
        run_home()

    with tab2:
        run_info()

    with tab3:
        run_eda()

    with tab4:
        run_ml()

    with tab5:
        run_stat()

if __name__ == '__main__':
    main()