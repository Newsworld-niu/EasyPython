import pandas as pd

def fix_time(data_date):
    if data_date[2] == '/' :
        copy_date = data_date.split('/')
        return f"{copy_date[2]}/{copy_date[1]}/{copy_date[0]}"
    return data_date

df = pd.read_csv('data/Student_Data_Messy.csv')

df = df.bfill()

df = df.drop(df[df['age'] <= 0].index)
df = df.drop(df[df['height'] <=0].index)
df = df.drop(df[df['weight'] <=0].index)
df = df.drop(df[df['score_math'] <=0].index)
df = df.drop(df[df['score_english'] <=0].index)
df['gender'] = df['gender'].str.replace('男', 'M')
df['gender'] = df['gender'].str.replace('女', 'F')
df['city'] = df['city'].str.replace('BJ', 'Beijing')
df['city'] = df['city'].str.replace('beijing', 'Beijing')
df['income'] = df['income'].str.replace('￥', '')
df['enroll_date'] = df['enroll_date'].str.replace('-', '/')
df['enroll_date'] = df['enroll_date'].apply(fix_time)
df.to_csv('data/Student_Data_Messy.csv', index=False)

