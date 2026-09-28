
# 3-1. with 블록 — 리소스를 안전하게 닫기
# 예전 방식 — 매번 f.close()를 신경써야 함
# f = open("security_log.txt", "w", encoding="utf-8")
# f.write("Admin login detected")
# f.close()

# with 블록 방식 — 실무에서는 이 방식을 사용
# with open("security_log0.txt", "w", encoding="utf-8") as f:
#     f.write("Admin login detected - 확인 00")
    
    
# 에러가 나도, return을 해도, 그냥 블록만 끝나면 파일은 안전하게 닫힘!
# print("파일이 자동으로 닫혔습니다.")

# 예전 방식 — 매번 f.close()를 신경써야 함
# f = open("security_log.txt", "w", encoding="utf-8")
# try:
#     f.write("Admin login detected")
#     # result = 10 / 0
# # except:
# except Exception as e:
#     print("에러 발생!")
# finally:
#     f.close()



## 3-2. CSV 파일 쓰기 — 일일 보안 점검 리포트

# import csv

# # 점검 데이터 (헤더 포함)
# report_data = [
#     ["호스트명", "IP_Address", "Status", "Last_Check"],
#     ["prd-web-01", "192.168.1.10", "Safe", "2026-08-29"],
#     ["prd-db-02", "192.168.1.20", "Vulnerable", "2026-08-29"],
#     ["prd-api-04", "192.168.1.30", "Safe", "2026-08-29"]
# ]

# # CSV 파일 저장
# # 기존내용추가 a 덮어쓰기는 w
# # utf 8이라 한글 안깨짐 (대신 엑셀은 깨진대 엑셀 이상한놈아! 뭔데!!!)
# # utf-8-sig : 엑셀에서 한글 안깨지는 인코딩
# with open("daily_security.scv", "a", newline='', encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(report_data)

# print("CSV 보고서 생성이 완료되었습니다.")





## 3-3. 딕셔너리를 이용한 쓰기(DictWriter) — 침입 탐지 로그
# import csv

# # 딕셔너리 형태의 IDS/IPS 탐지 로그
# logs = [
#     {"target": "방화벽", "event": "포트 스캔", "severity": "High"},
#     {"target": "IPS", "event": "SQL Injection", "severity": "Critical"},
#     {"target": "WAF", "event": "XSS Attempt", "severity": "Medium"}
# ]

# fieldnames = ["target", "event", "severity"]   # 엑셀의 맨 위 '열 이름' 정의

# with open("daily_log.csv", "w", newline='', encoding="utf-8-sig") as f:
#     writer = csv.DictWriter(f, fieldnames) # 뒤에 필드네임 줘야한다
#     writer.writeheader()
#     writer.writerows(logs)



# [ 연습 ] daily_security_report.csv 파일을 읽어서 Status가 "Vulnerable"인 취약한 호스트를 찾아 호스트 이름과 IP 주소를 출력하는 코드를 아래에 작성하세요
# with open("daily_security.csv", "r", newline='', encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     # print(list(reader))
#     for row in reader:
#         if row['Status'] == 'Vulnerable':
#             print(f'취약 발견: {row["Hostname2"]} : {row["IP_Address"]}')




# 3-4. 파이썬 객체로 JSON 만들기 — json.dumps()
# import json

# # 보안 점검 결과 데이터 (파이썬 딕셔너리)
# scan_result = {
#     "target": "10.0.1.50",
#     "status": "Critical",
#     "open_ports": [22, 80, 443],
#     "is_admin_exposed": True
}

# [1] 문자열로 변환 (indent는 가독성을 위한 들여쓰기)
# json_str = json.dumps(scan_result, indent=4)
# print(json_str)

# [2] 파일로 직접 저장하기 — 슬랙 웹훅 전송이나 다음 배치 스크립트가 읽음
# with open("scan_report.json", "w", encoding="utf-8") as f:
#     json.dump(scan_result, f, indent=4)


'''
dump()  vs  dumps()
s 는 string, 문자열
'''

# 3-5. JSON을 파이썬 객체로 읽기 — json.loads()
# with open("scan_report.json", "r", encoding="utf-8") as f:
#     file_data = json.load(f)
#     print(file_data['target'])