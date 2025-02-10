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
    font_dirs = [os.getcwd()]
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

    st.text('')
    st.text('')

    # 제목
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            📊 과거 데이터 확인하기
        </h2>
        <p style="font-size: 24px; text-align: center; color: ##4C82C2;">
            <b>탐색적 데이터 분석 (EDA)<b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 데이터 불러오기
    st.info("📌 **기본 데이터** (new_movie.csv) : 불필요 데이터 삭제 및 클러스터링 완료")
    df = pd.read_csv("data/new_movie.csv", index_col=0)
    df["영화 유형"].replace([0, 1, 2], ["미들 마켓", "메가 블록버스터", "블록버스터"], inplace=True)
    df["상영 등급"].replace(['G', 'PG', 'PG-13', 'R'], ['전체 관람가', '12세 이상 관람가', '15세 이상 관람가', '청소년 관람 불가'], inplace=True)
    df["개봉 연도"] = df["개봉 연도"].astype(str)
    
    # 데이터프레임 출력
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # 기본 통계 데이터 버튼
    if st.button("📈 기본 통계 데이터 보기"):
        st.dataframe(df.describe())

        st.info("""
                * count : 전체 데이터 수
                * mean : 평균값
                * std : 표준편차
                * min : 최솟값
                * 25% : 최솟값으로부터 1/4 지점의 값
                * 50% : 중앙값
                * 75% : 최솟값으로부터 3/4 지점의 값
                * max : 최댓값
                """)

    st.markdown("---")

    # 최대/최소 데이터 확인
    st.info("📌 **최대/최소 데이터 확인하기**")

    menu2 = ["제작 비용 ($)", "북미 박스오피스 수익 ($)", "전세계 박스오피스 수익 ($)", "개봉 주말 수익 ($)", "상영관 수", "상영 시간", "개봉 연도"]
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
    df_yearly = df.groupby("개봉 연도")["전세계 박스오피스 수익 ($)"].mean()
    fig1 = plt.figure()
    df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
    plt.ylabel("평균 수익 ($)")
    plt.xlabel("연도")
    plt.title("연도별 평균 수익")
    st.pyplot(fig1)

    st.write("""
        
    """)

    st.markdown("---")

    # 장르별 평균 수익 비교
    st.info("🎭 **장르별 평균 전 세계 수익 비교**")
    df_genre = df.groupby("장르")["전세계 박스오피스 수익 ($)"].mean().sort_values()
    fig2 = plt.figure()
    df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
    plt.xlabel("평균 수익 ($)")
    plt.ylabel("장르")
    plt.title("장르별 평균 수익")
    st.pyplot(fig2)

    st.markdown("---")

    # MPAA 등급별 수익 비교
    st.info("🎬 **상영 등급별 평균 전 세계 수익 비교**")
    df_mpaa = df.groupby("상영 등급")["전세계 박스오피스 수익 ($)"].mean().sort_values()
    fig3 = plt.figure()
    df_mpaa.plot(kind="bar", figsize=(8, 5), color="lightgreen")
    plt.ylabel("평균 수익 ($)")
    plt.xlabel("상영 등급")
    plt.xticks(rotation = 0)
    plt.title("상영 등급별 평균 수익")
    st.pyplot(fig3)

    st.markdown("---")

    # 상영관 수 vs 개봉 주말 수익 관계
    st.info("🏛 **상영관 수 vs 개봉 주말 수익 관계 분석**")
    fig4 = plt.figure(figsize=(8, 6))
    sb.scatterplot(x=df["상영관 수"], y=df["개봉 주말 수익 ($)"], alpha=0.5, color='purple')
    plt.xlabel("상영관 수")
    plt.ylabel("개봉 주말 수익 ($)")
    plt.title("상영관 수와 개봉 주말 수익의 관계")
    st.pyplot(fig4)

    st.markdown("---")