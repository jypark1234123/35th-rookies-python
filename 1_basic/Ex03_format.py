


# -----------------------------------------
#  1.  문자열 포맷
#name = "홍길동" 
#age = 20 
#print(f"이름: {name}, 나이: {age}")

#print("이름: {}, 나이: {}".format(name, age))
#print("이름2: {}, 나이: {}".format(name, age))
#print("이름3: {}, 나이: {}".format(name, age))

#print("이름: %s, 나이: %d" % (name, age))

#print("이름:", name, ", 나이:", age) # format 형식 출력 아님


# [1-1]. 문자열 포맷팅
#user = "홍길동"
#target = "192.168.10.5"
#action = "Login Failed"
# [보안알림] 사용자 홍길동가 192.168.10.5 서버에 Login Failed 하였습니다.
#message = f"# [보안알림] 사용자 {user}가 {target} 서버에 {action} 하였습니다."
#print(message)

# 포멧함수?

# [1-2]. 숫자 포맷팅
# age = 25
# score = 95
# print(f"나이: {age}세")
# print(f"점수: {score}점")

# 천 단위 쉼표 표시
# money=12345678
# print(f'금액: {money:,}원')


# 자릿수지정 : 서버번호-00X

# server_number = 3
# print(f'서버 번호-{server_number:03d}')


# [1-3]. 실수 포맷팅
# cpu_usage = 33.233
# print(f'CPU 사용률 : {cpu_usage:.2f} %')

# mem_usage = 48.28421
# print(f'메모리 사용률 : {mem_usage:.1f} %')





#--------------------------------
# 2. 입력받기

# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))
# height = float(input("키를 입력하세요: "))
# print(f"이름: {name}, 나이: {age}, 키: {height}")

'''
    [연습문제]
    서버이름(web)과 서버번호(1)를 입력받아 아래와 같이 출력되도록 하세요.

    [출력결과]
    서버: web-0001
'''
# server_name = input("서버 이름을 입력하세요: ")
# server_num = int(input("서버 번호를 입력하세요: "))
# print(f"서버: {server_name}-{server_num:04d}")




#--------------------------------
# 3. 임의의 수
import random

server_id1 = random.randint(1,45)
print(f'임의의 서버 번호: {server_id1:03d}')

server_id2 = random.uniform(1,45)
print(f'임의의 서버 번호: {server_id2:.2f}')