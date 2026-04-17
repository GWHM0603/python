# ===== ===== ===== ===== ===== 
# >>> 함수 실습
# ===== ===== ===== ===== ===== 

# >>> 사용자가 지정한 범위의 숫자들 중에서 
# >>>  짝수인 숫자만 합계해서 반환하는 함수
# >>> 예시: 5, 10 -> 범위에서 2의 배수만 합계
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

def even(a, b):
    result = 0
    for i in range(a, b + 1):
        
        if i % 2 == 0:
            result += i
    return result


# >>> 전달받은 단어의 2진수 형태를 출력해주는 함수

str1 = input("문자를 입력하세요: ")

# def str_binary(str1):
#     code =""
#     for i in str1:
#         code =  code + bin(ord(i))[2:]
#     print(code)

# >>> 컴프리헨션 버전
def str_binary(str1):
    code =[bin(ord(i))[2:] for i in str1]
    print(code) 
    code = " ".join(code)
    print(code)

str_binary(str1)