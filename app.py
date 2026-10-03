import streamlit as st
import pandas as pd
import plotly.express as px

# 设置页面布局
st.set_page_config(page_title='招聘岗位数据分析', layout='wide')
st.title('📊 招聘岗位数据分析工具')

# 读取清洗好的数据
df = pd.read_csv('data/clean_jobs.csv')

# ================= 侧边栏筛选 =================
st.sidebar.header('筛选条件')
# 城市多选（默认全选）
cities = st.sidebar.multiselect('选择城市', df['城市'].unique(), default=df['城市'].unique())
if cities:
    df = df[df['城市'].isin(cities)]

# 学历单选
edu_options = ['全部'] + list(df['学历要求'].unique())
edu = st.sidebar.selectbox('选择学历', edu_options)
if edu != '全部':
    df = df[df['学历要求'] == edu]

# ================= 主区域展示 =================
# 1. 核心指标卡片
col1, col2, col3 = st.columns(3)
col1.metric('岗位总数', len(df))
col2.metric('平均月薪', f'{df["salary_avg"].mean():.1f}K')
col3.metric('中位月薪', f'{df["salary_avg"].median():.1f}K')

# 2. 绘制图表（拆成两列）
col_left, col_right = st.columns(2)

with col_left:
    st.subheader('🏙️ 各城市岗位数量')
    city_counts = df['城市'].value_counts()
    fig1 = px.bar(x=city_counts.index, y=city_counts.values,
                  labels={'x': '城市', 'y': '岗位数量'})
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader('🛠️ 技能需求 Top10')
    skills = df['技能要求'].str.split('/').explode()
    skill_counts = skills.value_counts().head(10)
    fig2 = px.bar(x=skill_counts.values, y=skill_counts.index, orientation='h',
                  labels={'x': '出现次数', 'y': '技能'})
    st.plotly_chart(fig2, use_container_width=True)

# 3. 薪资分布（全宽）
st.subheader('💰 薪资分布')
fig3 = px.histogram(df, x='salary_avg', nbins=10,
                    labels={'salary_avg': '平均月薪 (K)'})
st.plotly_chart(fig3, use_container_width=True)

# 4. 原始数据展示
st.subheader('📋 详细数据')
st.dataframe(df)