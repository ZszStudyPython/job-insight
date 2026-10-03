import pandas as pd
import plotly.express as px

# 1. 读取清洗后的数据
df = pd.read_csv('data/clean_jobs.csv')

# 2. 画图：各城市岗位数量（柱状图）
city_counts = df['城市'].value_counts()
fig1 = px.bar(x=city_counts.index, y=city_counts.values,
              title='各城市岗位数量',
              labels={'x': '城市', 'y': '岗位数量'})
fig1.write_html('chart_city.html')  # 保存为网页文件

# 3. 画图：技能需求 Top10（横向柱状图）
skills = df['技能要求'].str.split('/').explode()
skill_counts = skills.value_counts().head(10)
fig2 = px.bar(x=skill_counts.values, y=skill_counts.index, orientation='h',
              title='技能需求 Top10',
              labels={'x': '出现次数', 'y': '技能'})
fig2.write_html('chart_skill.html')  # 保存为网页文件

# 4. 画图：薪资分布（直方图）
fig3 = px.histogram(df, x='salary_avg', nbins=10,
                    title='薪资分布',
                    labels={'salary_avg': '平均月薪 (K)'})
fig3.write_html('chart_salary.html')  # 保存为网页文件

print("图表生成成功！请去左侧项目文件夹，双击 HTML 文件查看。")
import pandas as pd
import plotly.express as px

# 1. 读取清洗后的数据
df = pd.read_csv('data/clean_jobs.csv')

# 2. 画图：各城市岗位数量（柱状图）
city_counts = df['城市'].value_counts()
fig1 = px.bar(x=city_counts.index, y=city_counts.values,
              title='各城市岗位数量',
              labels={'x': '城市', 'y': '岗位数量'})
fig1.write_html('chart_city.html')  # 保存为网页文件

# 3. 画图：技能需求 Top10（横向柱状图）
skills = df['技能要求'].str.split('/').explode()
skill_counts = skills.value_counts().head(10)
fig2 = px.bar(x=skill_counts.values, y=skill_counts.index, orientation='h',
              title='技能需求 Top10',
              labels={'x': '出现次数', 'y': '技能'})
fig2.write_html('chart_skill.html')  # 保存为网页文件

# 4. 画图：薪资分布（直方图）
fig3 = px.histogram(df, x='salary_avg', nbins=10,
                    title='薪资分布',
                    labels={'salary_avg': '平均月薪 (K)'})
fig3.write_html('chart_salary.html')  # 保存为网页文件

print("图表生成成功！请去左侧项目文件夹，双击 HTML 文件查看。")