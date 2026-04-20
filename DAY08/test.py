## =====================================================================
##                              복습  &  테스트
##                                                          2026-04-20
## ===================================================================== 
## [문제] 4칙 연산 계산기를 구현하세요.
## -> 기능 : 숫자 덧셈, 뺄셈, 곱셈, 나눗셈
## -> 조건 
##   ① 기능은 함수화
##   ② 2개 숫자 입력 받기
##   ③ 연산자 입력 받기
##   ④ x, X 입력 시 종료
## ===================================================================== 

def calculator(n1, n2, but_):
    if but_ == '+':
        return n1 + n2
    elif but_ == '-':
        return n1 - n2
    elif but_ == '*':
        return n1 * n2
    elif but_ == '/':
        if n2 == 0:
            return "은 잘못된 수식입니다. 0으로 나눌 수 없습니다."
        else:
            return n1 / n2

def checknum(n):
    if n.count('.') > 0:
        return float(n)
    else:
        return int(n)

while True:
    num1 = input("첫 번째 숫자를 입력하세요: ").strip()
    if num1:
        if num1 == 'x' or num1 == 'X':
            print("계산을 종료합니다.")
            break
        else:
            if num1.replace('.', '', 1).isdigit():
                num2 = input("두 번째 숫자를 입력하세요: ").strip()
                
                if num2:
                    if num2 == 'x' or num2 == 'X':
                        print("계산을 종료합니다.")
                        break
                        
                    else:
                        if num2.replace('.', '', 1).isdigit():
                            button = input("사칙 연산 기호를 입력하세요: ").strip()
                                
                            if button:
                                if button == 'x' or button == 'X':
                                    print("계산을 종료합니다.")
                                    break
                                else:
                                    if button == '+' or button == '-' or button ==  '*' or button == '/':
                                        num1 = checknum(num1)
                                        num2 = checknum(num2)
                                        result = calculator(num1, num2, button)
                                        print(f"{num1} {button} {num2} = {result}")
                                    else:
                                        print("잘못된 기호를 입력했습니다. 다시 입력하세요.")
                            else:
                                print("입력되지 않았습니다. 다시 입력하세요.")
                        else:
                            print("숫자가 입력되지 않았습니다.")
                else:
                    print("입력되지 않았습니다. 다시 입력하세요.")
            else:
                print("숫자가 입력되지 않았습니다.")
    else:
        print("입력되지 않았습니다. 다시 입력하세요.")