import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 한글 폰트 관련용도

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


# 월별 대출금리 변화 데이터 프레임 설정
df1['datetime'] = df1['날짜'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m'))     # 월별로 데이터 구성
df1.set_index('datetime', inplace=True)

# 월별 물건금액(만원) 데이터 프레임 설정
df_v = pd.DataFrame(df, columns=['계약일', '물건금액(만원)'])
df_v['계약일'] = df_v['계약일'].astype(str)
df_v['계약일'] = pd.to_datetime(df_v['계약일'])
df_v['date_ym'] = df_v['계약일'].dt.strftime("%Y-%m")      # 월별로 데이터 구성
df_mv = df_v.groupby('date_ym')['물건금액(만원)'].mean()  # 연도 월별에 따른 물건금액 평균

# 월별 대출금리 변화 꺾은선그래프
fig = plt.figure(figsize=(16,9))    # 그래프 크기 조정
ax1 = fig.add_subplot(2,1,1)
ax1.plot(df1['대출평균'], label ='대출평균', color='maroon')    # 보고자 하는 데이터 추가
ax1.plot(df1['가계대출'], label ='가계대출', color='darkorange')
ax1.plot(df1['주택담보대출'], label ='주택담보대출', color='gold')
ax1.plot(df1['보증대출'], label ='보증대출', color='skyblue')
ax1.set_title("월별 대출금리 변화", fontsize=14)  # 그래프 제목 설정
ax1.set_xlabel('날짜', fontsize=11)   # x축 라벨 설정
ax1.set_ylabel('연리(%)', fontsize=11)    # y축 라벨 설정
ax1.grid(axis='y', color ='gray', linestyle='--', linewidth=0.8)    # 격자 설정
ax1.legend(fontsize=14, loc='best')

# 월별 물건금액(만원) 꺾은선그래프
ax2 = fig.add_subplot(2,1,2)
ax2.plot(df_mv, color='skyblue')
ax2.set_title("월별 부동산 값 변화", fontsize=14)   # 그래프 제목
ax2.set_xlabel('날짜', fontsize=11)   # x축 label 설정
ax2.set_xticks([0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])   # x축 눈금 글자설정
ax2.set_ylabel('물건금액(만원)', fontsize=12)     # y축 label 설정
ax2.grid(axis='y', color ='gray', linestyle='--', linewidth=0.8)    # 격자 설정

plt.show()