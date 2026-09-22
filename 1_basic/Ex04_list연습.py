

alerts = ['로그인 실패', '포트 스캔 탐지', '악성 파일 탐지', '비정상 접속', 'DDoS 공격 탐지'] 

print(alerts)


# (1) `'SQL Injection 탐지'`, `'Brute Force 공격 탐지'`를 한꺼번에 리스트 마지막에 추가하세요.

# (2) `alerts` 리스트의 마지막 요소를 제거하세요.

# (3) `'SQL Injection 탐지'`, `'Brute Force 공격 탐지'`를 다시 한꺼번에 추가하세요.

# (4) `'SQL Injection 탐지'` 요소를 리스트에서 제거하세요.

# (5) `alerts` 리스트의 네 번째 위치(인덱스 3)에 `'랜섬웨어 탐지'`를 추가하세요.

# (6) `alerts` 리스트에서 3번째 요소부터 5번째 요소까지(인덱스 3~5)를 추출하여 출력하세요.

alerts.extend(['SQL Injection 탐지', 'Brute Force 공격 탐지'])
print('(1) 추가\n', alerts)

alerts.remove(alerts[-1])
print('(2) 마지막 요소 제거\n', alerts)

alerts.extend(['SQL Injection 탐지', 'Brute Force 공격 탐지'])
print('(3) 다시 추가\n', alerts)

alerts.remove('SQL Injection 탐지')
alerts.remove('SQL Injection 탐지')
print('(4) SQL Injection 탐지 제거\n', alerts)

alerts.insert(3, '랜섬웨어 탐지')
print('(5) 랜섬웨어 탐지 추가\n', alerts)

print(f'(6) 3번째부터 5번째까지 출력\n', alerts[3:6])

#---------------------------------------
# [ 최종결과 ]
# ['로그인 실패', '포트 스캔 탐지', '악성 파일 탐지', '랜섬웨어 탐지', 
#  '비정상 접속', 'DDoS 공격 탐지', 'SQL Injection 탐지', 'Brute Force 공격 탐지']