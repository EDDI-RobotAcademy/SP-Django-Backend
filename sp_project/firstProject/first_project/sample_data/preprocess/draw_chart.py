import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 엑셀 파일 읽기
df = pd.read_excel('travel_orders_data.xlsx')

# 주문날짜(str) -> datetime으로 변환
df['registerDate'] = pd.to_datetime(df['registerDate'])

# 그래프 설정
plt.figure(figsize=(14, 8))

# unique accountId의 수를 기반으로 색상맵 생성
unique_accounts = df['accountId'].unique()
colors = plt.cm.get_cmap('tab20', len(unique_accounts))

# 각 accountId별로 선 그리기
for i, account in enumerate(unique_accounts):
    account_data = df[df['accountId'] == account]
    plt.plot(account_data['registerDate'], [i] * len(account_data), color=colors(i), linestyle='-', linewidth=2, marker='o', markersize=5, markerfacecolor='white', label=f'Account {account}')

# 그래프 제목과 축 레이블 설정
plt.title('주문 동향', fontsize=16)
plt.xlabel('주문 날짜', fontsize=14)
plt.ylabel('고객 ID', fontsize=14)

# y축을 accountId 값으로 설정
plt.yticks(range(len(unique_accounts)), unique_accounts, fontsize=10)

# x축 레이블을 더 읽기 쉽게 회전
plt.xticks(rotation=45, fontsize=10)

# 그리드 추가
plt.grid(True, linestyle='--', alpha=0.6)

# 범례 추가
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# 그래프 표시
plt.tight_layout()
plt.show()
