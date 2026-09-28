'''
매일 새벽 실행되는 취약점 스캐너
-> 작업 폴더에 vuln_scan.log 파일 생성
-> 즉시 archive 폴더로 옮겨 보관

나열된 열린 포트 중 사내 보안 정책상 "안전 포트" 등록되지 않으면
CVS 취약점 리포트 / 시스템 연동용 JSON 알림 파일로 변환
'''
from pathlib import Path

# 사전 준비

# 실무형 취약점 스캔 로그 데이터 생성
log_data = """Scan Time: 2026-09-28 02:00:11
Target: 10.0.2.15
Port: 21 STATUS: OPEN
Port: 22 STATUS"""