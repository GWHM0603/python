# ===== ===== ===== ===== =====
# >>> 조건부 표현식
# >>> 여러 라인의 if-else 구문을 간단하게 표현
# >>> 형식: 조건 True일 때 실행 코드 if 조건식 else 조건 False일 때 실행코드
# ===== ===== ===== ====== ======


# >>> 짝수 홀수 판별 조건문
# >>> 기본

# while True:
#     num = input().strip()

#     if len(num):
#         if num.isdecimal():
#             num = int(num)

#             if num % 2:
#                 print(f"{num}: 홀수")
#             else:
#                 print(f"{num}: 짝수")

#         else:
#             print("잘못된 데이터입니다. 다시 입력하세요.\n")
#     print("입력이 되지 않았습니다. 다시 입력하세요.")

# ----- ----- ----- ----- -----


# >>> 조건부 표현식

while True:
    num = input("숫자를 입력하세요: ").strip()

    if len(num):
        if num.isdecimal():
            num = int(num)

            print(f'{num}: {"홀수" if num % 2 else "짝수"}')
            break

        else:
            print("잘못된 데이터입니다. 다시 입력하세요.\n")
            
    print("입력이 되지 않았습니다. 다시 입력하세요.\n")
print()

# ===== ===== ===== ===== =====


# >>> 음수, 0, 양수 판별 조건문 -> 다중 조건문
# >>> 기본문


num  = 5

if num > 0:
    print(f"{num}: 양수")
elif num < 0:
    print(f"{num}: 음수")
else:
    print(f"{num}: 0")
print()


# ----- ----- ----- ----- -----
# >>> 중복 제거


num  = 5
print(f'{num}: {"양수" if num > 0 else "음수" if num > 0 else "0"}')


# ===== ===== ===== ===== =====