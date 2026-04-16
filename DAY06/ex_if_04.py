# >>> 짝수 홀수 판별 출력
while True:

    num = input("숫자를 입력하세요: ").strip()
    print()

    if len(num):
        if num.isdecimal():
            num = int(num)
    
            if not num % 2:
                print(f"{num}은 짝수")
                break
            else:
                print(f"{num}은 홀수")
                break
        else:
            print("잘못된 형식을 입력하셨습니다.\n")
    else:
        print("입력이 되지 않았습니다.\n")
