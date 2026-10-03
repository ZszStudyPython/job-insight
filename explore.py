import pandas as pd

# 读取我们准备好的数据
df = pd.read_csv('data/jobs.csv')

# 打印数据形状（行数, 列数）
print("数据形状:", df.shape)

# 打印所有列名
print("列名:", df.columns.tolist())

# 打印前5行看看长什么样
print("\n前5行数据:")
print(df.head())