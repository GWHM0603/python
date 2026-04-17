# ===== ===== ===== ===== =====
# 함수: def():
# ===== ===== ===== ===== =====

a = 3
def add1(a, b):
    return a + b
    print(a)
print(add1(2, 3))
print(a)


def add2(a, b):
    print(a + b)
add2(2, 3)


def add3(): # 매개변수 없는 함수에 파라미터 입력하면 에러
    print(3 + 2)
add3()


def add4():
    return 3 + 2
print(add4())