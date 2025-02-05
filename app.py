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
from ui.ml import run_ml

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/custom_fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)

# 한글 폰트 설정
def set_korean_font():
    plt.rcParams['axes.unicode_minus'] = False
    system_os = platform.system()

    if system_os == "Darwin":  # macOS
        plt.rcParams['font.family'] = "AppleGothic"
    elif system_os == "Windows":  # Windows
        plt.rcParams['font.family'] = "Malgun Gothic"
    else:  # Linux (Google Colab, Ubuntu 등)
        nanum_font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
        if os.path.exists(nanum_font_path):  # 시스템에 폰트가 있으면 적용
            plt.rcParams['font.family'] = "NanumGothic"
        else:
            st.warning("한글 폰트가 없습니다. NanumGothic을 설치해주세요.")

def main():
    fontRegistered()
    set_korean_font()

    # 메인 타이틀 꾸미기
    st.markdown(
        """
        <h1 style='text-align: center; color: #FF4B4B;'>
            🎬 영화 예상 수익 예측 앱
        </h1>
        """, unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # 사이드바 스타일 개선
    st.sidebar.image("assets/M.png", use_container_width=True)  # 로고 추가 가능
    st.sidebar.markdown("## 🔹 Navigation")
    
    menu = ['🏠 Home', '📊 EDA', '🤖 ML']
    choice = st.sidebar.radio("**메뉴 선택**", menu)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("📌 Created by CodeKookiz (https://codekookiz.imweb.me)")
    
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()