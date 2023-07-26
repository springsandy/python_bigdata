import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

mpl.rc('font', family='Malgun Gothic') #한글 폰트 지정
plt.rcParams['axes.unicode_minus'] = False #마이너스 기호 깨짐 방지

df1 = pd.read_csv('crime_data.csv', encoding='cp949')
# df1.head()
# df1.tail()
# df1.info()
# df1.index
# df1.columns

# df1['범죄대분류'].unique()
# df1.groupby(['범죄대분류']).count()

#범죄대분류별로 그룹화
df1_group = df1.groupby('범죄대분류').sum()
print(df1_group)