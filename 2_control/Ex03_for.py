## 3-1. range() — 포트 스캔 시뮬레이션
sum = 0
for i in range(1, 6):
    print(i)
    sum += i
print(f'합계: {sum}')
# 지정 범위만큼 반복문 실행

# 구구단
dan = int(input('구구단 단수를 입력> '))
for n in range(10):
	print(f'{n} * {dan} = {n*dan}')

# 21~25번 포트를 하나씩 점검
for port in range(21, 26):
    print(f"포트 {port} 점검 중...")
    
# 100단뒤 포트를 점검
for port in range(1, 1000, 100):
    print(f"포트 {port} 점검 중...")

## 3-2. 리스트 순회 — 스캔 대상 호스트 점검
scan_queue = ["prd-bastion-01", "prd-db-02", "prd-api-04"]

print("--- 전수 조사 시작 ---")
for host in scan_queue:
    print(f"[점검 중] 대상: {host} ... 연결 확인 완료")
print("--- 점검 종료 ---")


## 3-3. 딕셔너리 순회 — CVE 카드 일괄 점검
cve_inventory = {
    "CVE-2026-30112": {"host": "prd-db-02", "cvss": 8.1, "patched": False},
    "CVE-2026-11450": {"host": "prd-api-04", "cvss": 9.4, "patched": True},
}

for key, value in cve_inventory.items():
    print(key, '-', value)

for cve_id, detail in cve_inventory.items():
    status = "패치완료" if detail["patched"] else "미패치"
    print(f"{cve_id} | 호스트: {detail['host']} | CVSS: {detail['cvss']} | {status}")


## 3-4. enumerate() — 로그 줄 번호와 함께 위험 패턴 탐지
auth_logs = ["Login success", "Failed password for root", "Logout", "Failed password for admin"]

for i, item in enumerate(auth_logs):
    print(i,'번째', item)

for line_num, log in enumerate(auth_logs, start=1):
    if "Failed" in log:
        print(f"[경고] {line_num}번째 줄에서 보안 위협 감지: {log}")



#============================================
'''
[ 문제 1 ]— 
    for문과 range()를 사용해서 1번부터 20번 포트 중 
    '짝수 번호'만 "포트 2 스캔 예정", "포트 4 스캔 예정" 형태로 출력해 봅시다. 
    (range()의 세 번째 인자, 간격을 활용하세요.)
'''
for i in range(0, 20, 2):
    print(f'포트 {i} 스캔 예정')


'''
[ 문제 2 ]— 
    `servers = ["WEB-01", "DB-01", "DB-02", "APP-01"]` 리스트가 있습니다. 

순회하면서 이름에 `"DB"`가 포함된 서버의 개수를 세어 `"DB 서버 총 2대"`처럼 출력해 봅시다.
'''
servers = ["WEB-01", "DB-01", "DB-02", "APP-01"]

db_num = 0
for server in servers:
    if "DB" in server:
        db_num += 1
print(f'DB 서버 총 갯수: {db_num}개')


'''
[ 문제 3 ]— 
    auth_logs = ["Login success", "Failed password", "Failed password", "Login success", "Failed password"] 리스트가 있습니다. 
    enumerate()를 사용해서 "Failed"가 포함된 로그의 **줄 번호와 내용**을 함께 출력하고, 
    반복이 끝난 뒤 총 실패 횟수도 출력해 봅시다.
'''
auth_logs = ["Login success", "Failed password", "Failed password", "Login success", "Failed password"]

count = 0
for line, detail in enumerate(auth_logs):
    if "Failed" in detail:
        print(f'{line}줄, {detail}')
        count += 1
print(f'총 실패 횟수: {count}')


# 추가 문제
# 보안 점검 대상 서버 목록
servers = [
    {"name": "WEB-01", "port": 443},
    {"name": "WEB-02", "port": 80},
    {"name": "DB-01", "port": 3306},
    {"name": "WAS-01", "port": 8080}
]

print("# 보안 점검 대상 서버")