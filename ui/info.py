import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_info():
    # 제목 스타일
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            🖥️ 앱 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    



    st.header('')

    # 초기 세션 상태 설정
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # 올바른 비밀번호 설정
    CORRECT_PASSWORD = "1234"  # 실제 서비스에서는 더 안전한 방법을 사용하세요!

    # 비밀번호 입력 UI
    if not st.session_state.authenticated:
        password = st.text_input("비밀번호를 입력하세요:", type="password")
        if st.button("로그인"):
            if password == CORRECT_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("비밀번호가 틀렸습니다.")

    # 인증된 경우만 콘텐츠 표시
    if st.session_state.authenticated:
        st.success("✅ 인증되었습니다!")

        st.markdown(
            """
            <h2 style="text-align: center; color: #FF4B4B;">
                🛠️ 통계
            </h2>
            """, 
            unsafe_allow_html=True
        )

        st.markdown("---")

        # 설명 부분 스타일 개선
        st.markdown(
            """
            <p style="font-size: 24px; text-align: center;">
                <b>사용자의 영화 예측 기록을 표시합니다.<b>
            </p>
            """, 
            unsafe_allow_html=True
        )
        st.text('')

        df = pd.read_csv('data/result.csv')
        df['개봉 연도'] = df['개봉 연도'].astype(str)
        st.dataframe(df)
        st.subheader('')

        if not df.empty :
            # 연도별 평균 수익 시각화
            st.info("📅 **연도별 평균 전 세계 수익 분석**")
            df_yearly = df.groupby("개봉 연도")["전세계 예상 수익 ($)"].mean()
            fig1 = plt.figure()
            df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
            plt.ylabel("평균 수익 ($)")
            plt.xlabel("연도")
            plt.title("연도별 평균 수익")
            st.pyplot(fig1)

            st.markdown("---")

            # 장르별 평균 수익 비교
            st.info("🎭 **장르별 평균 전 세계 수익 비교**")
            df_genre = df.groupby("장르")["전세계 예상 수익 ($)"].mean().sort_values()
            fig2 = plt.figure()
            df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
            plt.xlabel("평균 수익 ($)")
            plt.ylabel("장르")
            plt.title("장르별 평균 수익")
            st.pyplot(fig2)

            st.markdown("---")

            # MPAA 등급별 수익 비교
            st.info("🎬 **상영 등급별 평균 전 세계 수익 비교**")
            df_mpaa = df.groupby("상영 등급")["전세계 예상 수익 ($)"].mean().sort_values()
            fig3 = plt.figure()
            df_mpaa.plot(kind="bar", figsize=(8, 5), color="lightgreen")
            plt.ylabel("평균 수익 ($)")
            plt.xlabel("상영 등급")
            plt.xticks(rotation = 0)
            plt.title("상영 등급별 평균 수익")
            st.pyplot(fig3)