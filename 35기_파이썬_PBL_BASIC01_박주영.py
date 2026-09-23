# 환경 설정 및 모듈 임포트
import os, random
from dotenv import load_dotenv
load_dotenv()
scanner = os.getenv("SCANNER_NAME", "Local-Scanner")

# 기초 데이터 선언
critical_hosts = ("WEB-01", "DB-01")
vuln_assets = [{"cve": "CVE-2026-1001", "host": "WEB-01", "patched": False},
               {"cve": "CVE-2026-1002", "host": "DB-01", "patched": True}]

# 입력 처리
new_cve = input("추가할 CVE ID: ")
new_host = input("추가할 대상 호스트: ")

vuln_assets.append({"cve": new_cve, "host": new_host, "patched": False})

# 데이터 수정
vuln_assets[0]["patched"] = True
vuln_assets[-1]["CVSS Score"] = random.uniform(0, 10)


# 포맷팅 출력
print(f'총 {len(vuln_assets)}건의 취약점에 대한 패치 점검을 수행합니다.')
print('------------------------------------------------------------------')
print(f'[스캐너 {scanner}] {vuln_assets[0]["cve"]} ({vuln_assets[0]["host"]}) 패치 상태: {vuln_assets[0]["patched"]}')
print(f'핵심 자산 여부: {vuln_assets[0]["host"] in critical_hosts}')
print('------------------------------------------------------------------')
print(f'[스캐너 {scanner}] {vuln_assets[1]["cve"]} ({vuln_assets[1]["host"]}) 패치 상태: {vuln_assets[1]["patched"]}')
print(f'핵심 자산 여부: {vuln_assets[1]["host"] in critical_hosts}')
print('------------------------------------------------------------------')
print(f'[스캐너 {scanner}] {vuln_assets[2]["cve"]} ({vuln_assets[2]["host"]}) 패치 상태: {vuln_assets[2]["patched"]}')
print(f'핵심 자산 여부: {vuln_assets[2]["host"] in critical_hosts} / 현재 위험도: {vuln_assets[2]["CVSS Score"]:.2f}')