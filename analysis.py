import pandas as pd

# 1. 读取我们刚清洗好的干净数据
df = pd.read_csv('data/clean_jobs.csv')

# 2. 城市岗位分布（看看哪个城市招人多）
print("--- 城市岗位分布 ---")
city_counts = df['城市'].value_counts()
print(city_counts)

# 3. 薪资统计（均值、中位数、最高/最低）
print("\n--- 薪资统计分析 ---")
print(df['salary_avg'].describe())

# 4. 学历要求占比
print("\n--- 学历要求占比 ---")
edu_pct = df['学历要求'].value_counts(normalize=True) * 100
print(edu_pct.round(1))

# 5. 技能词频 Top10（最核心的亮点！）
print("\n--- 技能需求 Top10 ---")
# 按斜杠拆分，展开成多行，再统计
skills = df['技能要求'].str.split('/').explode()
skill_counts = skills.value_counts().head(10)
print(skill_counts)

# 6. 多维度交叉分析：不同城市的平均薪资
print("\n--- 城市平均薪资 ---")
city_salary = df.groupby('城市')['salary_avg'].agg(['mean', 'median', 'count'])
print(city_salary.round(1))

# 7. 多维度交叉分析：不同经验的平均薪资
print("\n--- 不同经验的平均薪资 ---")
exp_salary = df.groupby('exp_num')['salary_avg'].mean()
print(exp_salary.round(1))