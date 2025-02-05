import streamlit as st, pandas as pd, seaborn as sb, matplotlib.pyplot as plt


def run_eda() :
    st.subheader('')
    
    st.header('EDA (탐색적 데이터 분석)')
    st.subheader('')

    st.info('축적된 과거 데이터')
    df = pd.read_csv('data/new_movie.csv', index_col=0)
    df['Group'].replace([0, 1, 2], ['미들 마켓', '메가 블록버스터', '블록버스터'], inplace=True)
    df['year'] = df['year'].astype(str)
    st.dataframe(df)
    st.text('')

    if st.button('기본 통계 데이터') :
        st.dataframe(df.describe())
    st.subheader('')

    st.info('상관 관계 분석')
    df_corr = df.corr(numeric_only = True)
    menu = ['차트로 보기', '수치로 보기']
    choice = st.radio('표시 방식을 선택하세요.', menu)
    if choice == menu[0] :
        fig1 = plt.figure()
        sb.heatmap(data = df_corr, annot = True, vmin = -1, vmax = 1, cmap = 'coolwarm')
        st.pyplot(fig1)
    elif choice == menu[1] :
        st.dataframe(df_corr)
    st.subheader('')

    st.info('최대/최소 데이터 확인하기')
    menu2 = ['production_cost', 'domestic_gross', 'worldwide_gross', 'opening_weekend', 'theaters', 'runtime', 'year']
    selected_columns = st.selectbox('컬럼 선택', menu2)
    st.text('최댓값 데이터')
    st.dataframe(df.loc[df[selected_columns] == df[selected_columns].max(), :])
    st.text('최솟값 데이터')
    st.dataframe(df.loc[df[selected_columns] == df[selected_columns].min(), :])
    st.subheader('')

    