import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
from matplotlib import rc

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '../custom_fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)

plt.rcParams['axes.unicode_minus'] = False
system_os = platform.system()
if system_os == "Darwin":  # macOS
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
elif system_os == "Windows":  # Windows
    font_path = "C:/Windows/Fonts/malgun.ttf"
else:  # Linux
    rc('font', family='NanumGothic')

def run_eda():
    fontRegistered()
    plt.rc('font', family='NanumGothic')

    # 제목 정리
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            📊 탐색적 데이터 분석 (EDA)
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 데이터 불러오기
    st.info("📌 **축적된 과거 데이터** (new_movie.csv)")
    df = pd.read_csv("data/new_movie.csv", index_col=0)
    df["Group"].replace([0, 1, 2], ["미들 마켓", "메가 블록버스터", "블록버스터"], inplace=True)
    df["year"] = df["year"].astype(str)
    
    # 데이터프레임 출력
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # 기본 통계 데이터 버튼
    if st.button("📈 기본 통계 데이터 보기"):
        st.dataframe(df.describe())

    st.markdown("---")

    # 상관 관계 분석
    st.info("🔍 **상관 관계 분석**")
    df_corr = df.corr(numeric_only=True)

    # 선택 메뉴
    choice = st.radio("📊 표시 방식을 선택하세요.", ["차트로 보기", "수치로 보기"], horizontal=True)

    if choice == "차트로 보기":
        fig1 = plt.figure(figsize=(10, 6))
        sb.heatmap(data=df_corr, annot=True, vmin=-1, vmax=1, cmap="coolwarm", linewidths=0.5)
        st.pyplot(fig1)
    else:
        st.dataframe(df_corr)

    st.markdown("---")

    # 최대/최소 데이터 확인
    st.info("📌 **최대/최소 데이터 확인하기**")

    menu2 = ["production_cost", "domestic_gross", "worldwide_gross", "opening_weekend", "theaters", "runtime", "year"]
    selected_column = st.selectbox("📌 비교할 컬럼 선택", menu2)

    # 최댓값 데이터
    st.markdown("✅ **최댓값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), :])

    # 최솟값 데이터
    st.markdown("✅ **최솟값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), :])

    st.markdown("---")

    # 연도별 평균 수익 시각화
    st.info("📅 **연도별 평균 전 세계 수익 분석**")
    df_yearly = df.groupby("year")["worldwide_gross"].mean()
    fig1 = plt.figure()
    df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
    plt.ylabel("평균 수익 ($)")
    plt.xlabel("연도")
    plt.title("연도별 평균 수익")
    st.pyplot(fig1)

    st.markdown("---")

    # 장르별 평균 수익 비교
    st.info("🎭 **장르별 평균 전 세계 수익 비교**")
    df_genre = df.groupby("genre")["worldwide_gross"].mean().sort_values()
    fig2 = plt.figure()
    df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
    plt.xlabel("평균 수익 ($)")
    plt.ylabel("장르")
    plt.title("장르별 평균 수익")
    st.pyplot(fig2)

    st.markdown("---")

    # MPAA 등급별 수익 비교
    st.info("🎬 **MPAA 등급별 평균 전 세계 수익 비교**")
    df_mpaa = df.groupby("mpaa")["worldwide_gross"].mean().sort_values()
    fig3 = plt.figure()
    df_mpaa.plot(kind="bar", figsize=(8, 5), color="lightgreen")
    plt.ylabel("평균 수익 ($)")
    plt.xlabel("MPAA 등급")
    plt.xticks(rotation = 0)
    plt.title("MPAA 등급별 평균 수익")
    st.pyplot(fig3)

    st.markdown("---")

    # 상영관 수 vs 개봉 주 수익 관계
    st.info("🏛 **상영관 수 vs 개봉 주 수익 관계 분석**")
    fig4 = plt.figure(figsize=(8, 6))
    sb.regplot(x=df["theaters"], y=df["opening_weekend"], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.xlabel("상영관 수")
    plt.ylabel("개봉 주 수익 ($)")
    plt.title("상영관 수와 개봉 주 수익 관계")
    st.pyplot(fig4)

    st.markdown("---")