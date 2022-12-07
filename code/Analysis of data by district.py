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

# 자치구 별 건물면적 당 금액(만원) 데이터 프레임 설정(내림차순)
df_m = df_value.groupby(['자치구명'], as_index=False).mean()  # 자치구별 평균 설정
df_mean = df_m.sort_values(by=['건물면적 당 금액(만원)'], ascending=False)  # 내림차순 설정

# 자치구 별 건물면적 당 금액(만원) 막대그래프
plt.figure(1)
sns.barplot(data=df_mean, x='자치구명', y='건물면적 당 금액(만원)')  # 막대그래프 설정
plt.title("자치구에 따른 건물면적(㎡) 당 금액", fontsize=15 )  # 그래프 제목 설정
plt.grid(axis='y', color ='purple', linestyle='--', linewidth=1)    # 격자 설정
plt.gcf().set_size_inches(16,9)    # 그래프 크기 조정

plt.show()
