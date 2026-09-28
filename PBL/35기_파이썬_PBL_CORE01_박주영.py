import random

# 데이터 준비
line_names = [f"LINE-{i:02d}" for i in range(1,13)]
raw_logs = [random.randint(1,100) for _ in range(10)] + [0, "Timeout", None, 99, "Error"]
random.shuffle(raw_logs)

print(raw_logs)
print('--- 실시간 네트워크 트래픽 점검 시작 ---')

# 반복 구조 설계
n = 0
for log in raw_logs:
    try:
        # 입력값이 실수인 경우
        # [99% - 비상 중단]
        # [95% 이상 - 심각]
        # [70% 이상 - 경고]
        # [0% - 확인 필요]

        raw_logs[n] = float(log)
        if log == 99:
            print(f'[EMERGENCY] {raw_logs[n]:.1f}% 감지! 대규모 DDoS 공격 의심으로 전체 점검 중단!')
            break
        elif log >= 95 and log < 99:
            print(f'[CRITICAL] 패킷 손실률 {raw_logs[n]:.1f}%: 즉시 회선 차단 및 우회 경로 전환')
        elif log >= 70 and log < 95:
            print(f'[WARNING] 패킷 손실률 {raw_logs[n]:.1f}%: 네트워크 관리자 호출 및 회선 점검 메시지 출력')
        elif log > 0 and log < 70:
            print(f'[NORMAL] 패킷 손실률 {raw_logs[n]:.1f}%: 회선 정상')
        else:
            print(f'[CHECK] 패킷 손실률 {raw_logs[n]}%: 트래픽 없음 (회선 다운 의심)')

    # 입력값이 실수가 아닌 경우
    except Exception as e:
        print(f'[DATA ERROR] 읽을 수 없는 로그 형식입니다. (입력값: {raw_logs[n]})')

    # 공통 마감 출력
    finally:
        print('--------------- 점검 완료 ---------------')
        n += 1

# 결과 요약
warning_logs= [logs for logs in raw_logs if isinstance(logs, float) and 70 <= logs < 99]
print(f'[요약] 위험(WARNING 이상) 손실률 목록: {warning_logs}')
