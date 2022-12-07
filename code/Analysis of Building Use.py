import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 한글 폰트 관련용도
import seaborn as sns

mpl.rcParams['axes.unicode_minus'] = False  # 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처

path = 'C:/Users/mingyu/Desktop/data/Transaction price of housing prices_seoul.csv'  # 주택 실거래가 데이터
path1 = 'c:/Users/mingyu//Desktop/data/Loan Interest Rate.csv'  # 대출금리 데이터
df = pd.read_csv(path, encoding='cp949', low_memory=False)  # 서울 실거래가 데이터 불러오기(데이터프레임 형태)
df1 = pd.read_csv(path1, encoding='cp949', low_memory=False)  # 대출금리 데티어 불러오기(데이터프레임 형태)
df1 = df1.dropna(axis=1)    # NaN값 제거

# 폰트 경로
font_path = 'C:/Windows/Fonts/H2GTRM.TTF'
# 폰트 이름 가져오기
font_name = fm.FontProperties(fname=font_path).get_name()
# 폰트 설정
mpl.rc('font', family=font_name)

df_value = pd.DataFrame(df, columns=['자치구명', '건물면적 당 금액(만원)'])
df_pp = pd.DataFrame(df, columns=['자치구명', '건물용도', '물건금액(만원)'])

# 지역구별 건물용도에 따른 금액
df_p = df_pp.groupby(['자치구명', '건물용도'], as_index=False).mean()  # 지역구별 건물용도에 따른 금액
df_purpose = df_p.sort_values(by=['물건금액(만원)'], ascending=False) # 내림차순 설정

# 각 건물용도 개수
df_kind = df['건물용도'].value_counts()     # 각 건물용도 개수 카운트
kind = ["아파트", "연립다세대", "오피스텔", "단독다가구"]

# 자치구 별 건물용도에 따른 금액(만원) 누적막대그래프
plt.figure(1)
sns.barplot(data=df_p, x='자치구명', y='물건금액(만원)', hue='건물용도' ,dodge=False)
plt.title("자치구 별 건물용도에 따른 금액(만원)", fontsize=15 )  # 그래프 제목 설정
plt.grid(axis='y', color ='purple', linestyle='--', linewidth=1)    # 격자 설정
plt.gcf().set_size_inches(16,9)    # 그래프 크기 조정

# 각 건물용도 개수(원 그래프)
fig = plt.figure(figsize=(16,9))    # 그래프 크기 조정
ax1 = fig.add_subplot(1,1,1)
ax1.pie(df_kind, autopct='%.1f%%', labels=kind, colors=['skyblue', 'pink', 'gray', 'lightgreen'], explode=[0.1, 0.1, 0.1, 0.1])
ax1.set_title("각 건물용도에 따른 개수", fontsize=15 )  # 그래프 제목 설정
ax1.legend(loc='center left')

plt.show()
