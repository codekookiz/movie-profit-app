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
        """, unsafe_allow_html=True
    )
    
    st.markdown("""<hr style="border: none; height: 5px; background: #5B9BD5; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);">""",
                 unsafe_allow_html=True)
    
    # 사이드바 스타일 개선
    st.sidebar.image("image/main_sidebar.png", use_container_width=True)  # 로고 추가 가능
    st.sidebar.markdown("## 🔹 찾아보기")
    
    menu = ['🏠 홈', '📊 과거 데이터 확인하기', '🎬 영화 수익 예측하기', 'ℹ 앱 정보',  '⚒️ 통계 데이터']
    choice = st.sidebar.radio("**메뉴 선택**", menu)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("📌 Created by CodeKookiz (https://codekookiz.imweb.me)")
    
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()
    elif choice == menu[3]:
        run_info()
    elif choice == menu[4]:
        run_stat()

if __name__ == '__main__':
    main()