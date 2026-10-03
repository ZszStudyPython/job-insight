import pandas as pd
import re

# 1. 读取数据
df = pd.read_csv('data/jobs.csv')
print("原始数据形状:", df.shape)

# 2. 薪资解析函数
def parse_salary(text):
    if pd.isna(text) or '面议' in str(text):
        return None, None, None
    nums = re.findall(r'(\d+\.?\d*)', str(text))
    if len(nums) >= 2:
        low, high = float(nums[0]), float(nums[1])
    elif len(nums) == 1:
        low = high = float(nums[0])
    else:
        return None, None, None
    if '万' in str(text):
        low *= 10
        high *= 10
    avg = (low + high) / 2
    return low, high, avg

# 3. 应用薪资解析，生成新列
df[['salary_min', 'salary_max', 'salary_avg']] = df['薪资'].apply(
    lambda x: pd.Series(parse_salary(x))
)

# ================= 下面是新增的清洗步骤 =================

# 4. 处理缺失值
print("\n薪资缺失数量:", df['salary_avg'].isnull().sum())
# 删除薪资缺失的行（面议的岗位没法参与薪资分析）
df = df.dropna(subset=['salary_avg'])
print("删除缺失薪资后形状:", df.shape)

# 5. 城市标准化（去掉“市”、“江苏”等字）
df['城市'] = df['城市'].astype(str).str.replace('市', '').str.replace('省', '').str.replace('江苏', '')
df['城市'] = df['城市'].str.strip() # 去除两边空格

# 6. 技能字段拆分（方便后面算词频）
# 把中文顿号、空格统一换成斜杠
df['技能要求'] = df['技能要求'].astype(str).str.replace('、', '/').str.replace('，', '/').str.replace(' ', '/')

# 7. 经验数值化（提取“3年以上”里的数字 3）
def parse_exp(text):
    if pd.isna(text) or '不限' in str(text) or '应届' in str(text):
        return 0
    nums = re.findall(r'(\d+)', str(text))
    if nums:
        return int(nums[0])
    return 0

df['exp_num'] = df['经验要求'].apply(parse_exp)

# ================= 清洗完成，保存 =================

# 8. 保存清洗后的数据
df.to_csv('data/clean_jobs.csv', index=False, encoding='utf-8-sig')
print("\n清洗完成！已保存至 data/clean_jobs.csv，共", len(df), "条有效数据")

# 9. 打印最终结果看看
print("\n清洗后的数据预览:")
print(df[['岗位名称', '城市', '薪资', 'salary_avg', '经验要求', 'exp_num', '技能要求']].head(5))