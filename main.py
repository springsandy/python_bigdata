import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from tabulate import tabulate

mpl.rc('font', family='Malgun Gothic') #한글 폰트 지정
plt.rcParams['axes.unicode_minus'] = False #마이너스 기호 깨짐 방지

#데이터 불러오기 및 데이터 정보 확인
df1 = pd.read_csv('crime_data.csv', encoding='cp949')
# print(df1.head()) #제일 앞에서 n개의 데이터 받아오기
# print(df1.tail()) #제일 뒤에서 n개의 데이터 받아오기
# print(df1.info()) #컬럼(열) 정보 받아오기
# print(df1.index)
# print(df1.columns) #컬럼의 이름만 출력

# print(df1['범죄대분류'].unique()) #'범죄대분류'의 카테고리
# print(df1['범죄대분류'].value_counts()) #'범죄대분류'의 각각 카테고리의 갯수
# print(df1['범죄중분류'].unique()) #'범죄중분류'의 카테고리

#범죄대분류별로 그룹화
df1_group_sum = df1.groupby('범죄대분류').sum() #'범죄대분류'의 카테고리 기준 합계
df1_group_sum = pd.DataFrame(df1_group_sum)
print(tabulate(df1_group_sum, headers='keys', tablefmt='psql', showindex=True))
# print(df1_group_sum['생활정도(계)']) #그 중에서도 '생활정도(계)'만 출력
# print(df1_group_sum[['생활정도(계)', '생활정도(하류)']]) #그 중에서도 '생활정도(계), '활정도(하류)' 출력

#범죄대분류별 합계 및 내림차순
df1_group = df1_group_sum.drop('범죄중분류', axis=1) #'범죄중분류'의 카테고리 삭제(데이터 값이 str값이라 에러 발생함)
df1_group = np.sum(df1_group, axis=1)
df1_group = pd.DataFrame(df1_group).reset_index() #인덱스 재설정
df1_group.rename(columns={0:'total'}, inplace=True) #컬럼명 변경
df1_group.sort_values(by='total', ascending=False, inplace = True) #'total'기준으로 내림차순 정렬
# print(df1_group)

#최다 빈도수의 번죄대분류 리스트 생성
crime_list = df1_group['범죄대분류'].tolist()
# print(crime_list)

#막대그래프 시각화
# plt.figure(figsize = (10, 5)) #그래프 크기 설정
# plt.rc('font', family='Malgun Gothic') #한글 폰트 지정
# plt.title('범죄대분류 상위 5개 범죄', fontsize=20) #그래프 제목 설정
#
# sns.set_style('darkgrid') #그래프 스타일 지정
# sns.barplot(data=df1_group, x='범죄대분류', y='total', order=crime_list[:5])
#
# plt.ylabel('총 빈도수', fontsize=15)
# plt.xlabel('범죄대분류', fontsize=15)
# plt.xticks(fontsize=13)
# plt.yticks(fontsize=13)
# plt.show()

#'강력범죄' 중 범죄중분류 최다 빈도수 분석
cond1 = (df1['범죄대분류'] == '강력범죄')
df2 = df1.loc[cond1].drop(columns='범죄대분류')
df2 = np.sum(df2.groupby('범죄중분류').sum(), axis=1)
df2 = pd.DataFrame(df2).reset_index()
df2.rename(columns={0:'합계'}, inplace=True)
df2.sort_values(by='합계', ascending=False, inplace = True)
# print(df2)

#막대그래프 시각화
# plt.figure(figsize = (10, 5)) #그래프 크기 설정
# plt.rc('font', family='Malgun Gothic') #한글 폰트 지정
# plt.title('강력범죄의 범죄중분류 건수', fontsize=18) #그래프 제목 설정
#
#
# sns.barplot(data=df2, y='범죄중분류', x='합계')
# sns.set_style('whitegrid') # 그래프 스타일 지정
#
# plt.xlabel('빈도수', fontsize = 13) # x축 제목 서식 설정
# plt.ylabel('범죄 종류', fontsize = 13) # y축 제목 서식 설정
# plt.xticks(fontsize = 15) # x축 레이블 서식 설정
# plt.yticks(fontsize = 10, rotation = 12) # y축 레이블 서식 설정
# plt.show()

#'지능범죄' 중 범죄중분류 최다 빈도수 분석
# mpl.rc('font', family='Malgun Gothic')
# plt.figure(figsize=(10, 5))
# plt.title('지능범죄 중 범죄중분류 건수', fontsize=20)
#
# sns.set_style('whitegrid')
# sns.despine(left=True, bottom=True)
# sns.barplot(data=df2, x='범죄중분류', y='합계')
#
# plt.xlabel('범죄 종류', fontsize=15)
# plt.ylabel('빈도수', fontsize=15)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.show()

#결혼 여부에 따른 범죄 건수
df1['혼인_합계'] = df1['혼인관계(유배우자)'] + df1['혼인관계(동거)']+ df1['혼인관계(이혼)']+ df1['혼인관계(사별)']
df1['미혼_합계'] = df1['미혼자부모관계(실(양)부모)'] + df1['미혼자부모관계(계부모)'] + df1['미혼자부모관계(실부계모)'] + df1['미혼자부모관계(실부무모)'] + df1['미혼자부모관계(실모계부)'] + df1['미혼자부모관계(실모무부)'] + df1['미혼자부모관계(계부무모)'] + df1['미혼자부모관계(계모무부)'] + df1['미혼자부모관계(무부모)']
# print(df1.head())

df3 = df1[['범죄중분류', '혼인_합계', '미혼_합계']].set_index('범죄중분류')
df3 = df3.drop('소계', axis=0)
df3.sort_values(by='혼인_합계', ascending=False, inplace=True)
# print(df3)

# ax = df3.sort_values(by='혼인_합계', ascending=False).plot(kind='bar', title='범죄분석', figsize=(16, 8), legend=True, fontsize=12)
# ax.set_xlabel('범죄중분류', fontsize=12)
# ax.set_ylabel('범죄건수', fontsize=12)
# ax.legend(['혼인_합계', '미혼_합계'], fontsize=12)
# plt.show()