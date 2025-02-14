import streamlit as st
import pandas as pd
from datetime import datetime, timedelta, timezone
import streamlit_option_menu as som
from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_lottie import st_lottie
import requests

from ui.dev import run_dev
from ui.eda import run_eda
from ui.home import run_home
from ui.info import run_info
from ui.ml import run_ml
from ui.stat import run_stat

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

def main():
    # 스타일링 적용
    st.markdown(
        """
        <style>
            h1 {
                text-align: center;
                color: #4C82C2;
                font-size: 2.5em;
                font-weight: bold;
            }
            h2 {
                text-align: center;
                color: #5B9BD5;
                font-size: 1.8em;
                margin-bottom: 20px;
            }
            .sidebar .block-container {
                padding: 1.5rem;
            }
            .metric-container {
                background: #F8F9FA;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }
            section[data-testid="stSidebar"] h3 {
                text-align: left !important;
            }
            div[data-testid="stOptionMenu"] button {
                font-size: 14px !important;
                padding: 8px 15px !important;
            }
        </style>
        """, unsafe_allow_html=True
    )
    
    # 메인 타이틀
    st.markdown("""
        <h1>🎬 영화 예상 수익 예측 앱</h1>
        <h2>🤖 머신러닝 기반</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""<hr style="border: none; height: 4px; background: #5B9BD5;">""", unsafe_allow_html=True)
    
    # 로고 추가
    st.sidebar.image("image/main_sidebar.png", use_container_width=True)
    
    # 현재 날짜 & 시간 표시
    kst_now = datetime.now(timezone.utc) + timedelta(hours=9)
    now_str = kst_now.strftime("%Y-%m-%d %a %H:%M %p")
    st.sidebar.markdown(f"🕒 **현재 시간:** {now_str}")
    st.sidebar.markdown("---")
    
    df = pd.read_csv('data/new_movie.csv')
    count = len(df)
    prod = int((df['제작 비용 ($)'].mean() / 1000000).round())
    prof = int((df['전세계 박스오피스 수익 ($)'].mean() / 1000000).round())
    best = df.sort_values('전세계 박스오피스 수익 ($)', ascending=False).iloc[0, :]['제목']
    
    # 영화 데이터 요약
    st.sidebar.markdown("### 📊 데이터 요약")
    
    with st.sidebar:
        col1, col2 = st.columns(2)
        col1.metric("📈 총 영화 데이터", f"{count}개")
        col2.metric("💰 평균 제작비", f"${prod}M")
        col3, col4 = st.columns(2)
        col3.metric("🎟 평균 수익", f"${prof}M")
        col4.metric("⭐️ 최고 흥행작", f"{best}")
    
    style_metric_cards(border_left_color="#4C82C2")
    
    st.sidebar.markdown("---")
    
    # 애니메이션 추가
    lottie_url = "https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json"
    lottie_json = load_lottie_url(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=150, key="lottie")
    
    # Option Menu 추가
    selected = som.option_menu(
        menu_title=None,
        options=["홈", "앱 정보", "개발", "데이터 분석", "수익 예측", "통계"],
        icons=["house", "info-circle", "tools", "bar-chart", "film", "database"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5px", "background-color": "#f9f9f9"},
            "icon": {"color": "#4C82C2", "font-size": "16px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "center",
                "margin": "0px",
                "padding": "5px 10px",
            },
            "nav-link-selected": {"background-color": "#5B9BD5"},
        }
    )

    # 선택한 메뉴에 따라 해당 함수 실행
    if selected == "홈":
        run_home()
    elif selected == "앱 정보":
        run_info()
    elif selected == "개발":
        run_dev()
    elif selected == "데이터 분석":
        run_eda()
    elif selected == "수익 예측":
        run_ml()
    elif selected == "통계":
        run_stat()
    
if __name__ == '__main__':
    main()