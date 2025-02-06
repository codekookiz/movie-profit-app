import streamlit as st

def run_info():
    # 제목 스타일
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            ℹ 앱 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 앱 개요
    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            앱 개요
        </h3>
        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        이 앱은 영화의 다양한 정보를 바탕으로 영화의 유형을 분류하고, 북미 박스오피스 수익을 예측한 후 이를 기반으로 전 세계 수익 예측까지 제공하는 웹 애플리케이션입니다.

        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        사용자는 영화의 제작비용, 개봉 주 수익, 상영 등급, 장르, 상영 시간, 개봉 연도 등의 정보를 입력하여, 해당 영화가 어떤 유형에 속하는지 확인하고, 예측된 북미 수익에 기반하여 전 세계 수익도 예측할 수 있습니다.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 예상 이용자
    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            예상 이용자
        </h3>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>🎬 영화 산업 종사자</b> : 영화 제작자, 배급사, 마케팅 팀 등은 영화의 성공 가능성을 예측하고, 예산 책정 및 마케팅 전략 수립을 위해 이 애플리케이션을 유용하게 사용할 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>💰 영화 투자자</b> : 영화에 투자하거나 자금을 지원하는 사람들은 예상 수익을 예측하여 투자 결정을 내리는 데 도움을 받을 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>🍿 영화 팬 및 관객</b> : 영화의 흥행 예측에 관심이 있는 영화 팬들은 개인적으로 좋아하는 영화의 성공 가능성을 예측하고 분석할 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>📊 데이터 분석 및 머신러닝 관심자</b> : 영화 데이터를 기반으로 예측 모델을 분석하고 연구하는 데이터 분석가나 머신러닝 엔지니어가 이 애플리케이션을 학습 및 실험용으로 사용할 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>🧑‍💻 영화 리뷰어 및 블로거</b> : 영화 관련 콘텐츠를 작성하는 사람들은 예측된 정보를 바탕으로 트렌드나 흥행 요소에 대해 더 깊은 분석을 제공할 수 있습니다.
        </ul>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 앱의 장점
    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        앱의 장점
    </h3>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 정확한 영화 예측</b> : 제작비용, 개봉 수익, 상영 등급, 장르, 상영 시간, 개봉 연도 등의 다양한 데이터를 기반으로 영화의 성공 가능성을 예측하여, 영화 제작자나 투자자에게 유용한 의사결정 정보를 제공합니다.<br>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 북미 및 전 세계 수익 예측</b> : 북미 박스오피스를 기반으로 한 예측을 통해, 영화의 전 세계 수익을 예측할 수 있어 글로벌 영화 시장을 이해하는 데 중요한 도구가 됩니다.<br>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 데이터 기반 의사결정 지원</b> : 사용자는 데이터 기반의 예측 결과를 바탕으로 마케팅 전략을 세우거나 투자 결정을 내리는 데 도움을 받을 수 있습니다. 이는 직관적인 판단을 넘어 객관적인 분석을 제공합니다.<br>
        <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 다양한 사용자층을 위한 접근성</b> : 영화 산업 종사자부터 영화 팬까지 다양한 사용자가 이 앱을 통해 자신에게 맞는 정보를 얻을 수 있습니다. 영화에 대한 관심도를 높이고 분석적인 접근을 가능하게 합니다.<br>
        <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 트렌드 분석</b> : 영화의 장르, 개봉 연도, 상영 시간 등을 고려한 분석으로 영화 시장의 트렌드를 예측하고, 더 나아가 영화 제작이나 마케팅에 대한 전략적 인사이트를 제공합니다.<br>
        <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 기술적 신뢰성</b> : 머신러닝 모델을 사용하여 예측을 제공하기 때문에, 과거의 데이터와 통계를 바탕으로 보다 신뢰성 있는 결과를 도출합니다. 이는 특히 영화 투자나 배급을 고민하는 사람들에게 큰 장점이 될 수 있습니다.
    </ul>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")

    # 앱 개발 과정
    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            앱 개발 과정
        </h3><br>

        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
            <b>1️⃣ 데이터 전처리 및 클러스터링</b><br>
            𝟙. Kaggle에서 제공하는 top-500-movies.csv 파일을 활용해 영화 데이터를 분석하였습니다.<br>
            𝟚. 문자열 데이터를 LabelEncoder로 변환 후, K-Means 클러스터링을 진행하여 영화의 유형을 분류하였습니다.<br>&nbsp;&nbsp;&nbsp;
            <i>- 클러스터의 개수는 최대 10개로 제한하고, 범위 내에서 최적의 클러스터 수를 확인했습니다.</i><br>
            𝟛. 엘보우 메소드를 통해 최적의 클러스터 수를 자동으로 도출하여, 영화의 유형을 3개의 클러스터로 분류했습니다.<br><br>

        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
            <b>2️⃣ 영화 유형 예측 모델</b><br>
            𝟙. KNeighborsClassifier를 사용해 영화 유형 분류 모델을 학습시켰습니다.<br>&nbsp;&nbsp;&nbsp;
            <i>- 이 때 Neighbors의 수는 5개로 설정했습니다.</i><br>
            𝟚. 이를 통해, 사용자가 입력한 영화 정보를 바탕으로 해당 영화가 어느 유형에 속하는지 예측할 수 있습니다.<br>
            𝟛. 모델의 정확도는 75.76%로 실사용이 가능한 수준으로 판단되었습니다.<br><br>

        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
            <b>3️⃣ 북미 수익 예측 및 전 세계 수익 예측</b><br>
            𝟙. 영화의 다양한 특성(제작비용, 개봉 수익 등)을 기반으로 LinearRegression, RandomForestRegressor, XGBRegressor 모델을 사용하여 북미 시장의 박스오피스 수익을 예측하였습니다.<br>
            𝟚. 학습과 테스트 결과, LinearRegression 모델이 73%라는 가장 높은 예측 정확도를 보였고, 따라서 이를 최종 모델로 선택했습니다.<br>
            𝟛. 북미 박스오피스 수익을 바탕으로 전 세계 수익을 예측하기 위해 수익 비율을 계산하고, 해당 비율을 기반으로 예측값을 제공할 수 있게 되었습니다.<br>&nbsp;&nbsp;&nbsp;
            <i>- 세계 성적/북미 성적 비율의 최소치가 1.1이고, 평균치가 3.5인데 반해 최댓값이 315.4에 달할 정도로 과도하게 높았습니다.<br>&nbsp;&nbsp;&nbsp;
            - 따라서, 해당 비율의 mean()값 대신 median()값을 '수익 비율'로 설정하여 예측값 제공을 위해 사용하기로 결정했습니다.</i>
        </p>
        """, 
    unsafe_allow_html=True
)
    
    st.markdown("---")
    
    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        배포 과정
    </h3><br>

    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        📤 앱은 Streamlit을 사용하여 웹 애플리케이션 형태로 배포되었습니다.<br>

    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        🖥️ 초기에는 로컬 환경에서 테스트 후, requirements.txt 파일을 생성하여 외부 환경에서도 실행 가능하도록 설정하였습니다.
    </p>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")

    st.header('')