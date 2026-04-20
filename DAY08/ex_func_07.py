# ===== ===== ===== ===== =====
# >>> 함수 이름: add_two
# >>> 함수 기능: 2개의 정수를 더한 후 결과 반환
# >>> 매개변수: num1, num2
# >>> 함수 결과: 덧셈 결과
# ===== ===== ===== ===== =====

def add_two_int(num1 = 1, num2 = 1):
    value = num1 + num2
    return value

print(add_two_int(1, 2))
print(add_two_int())
print(add_two_int(3))

# ===== ===== ===== ===== =====
# >>> 함수 이름: save_name_gender
# >>> 함수 기능: 이름과 성별을 입력받아 출력하기. 성별 기본은 남성.
# >>> 매개변수: gender, name
# >>> 함수 결과: 없음.
# ===== ===== ===== ===== =====
# def save_name_gender(gender = '남', name): -> ERROR 
def save_name_gender(name, gender = '남'): # default 매개변수는 뒤로 보낸다.
    print(name, gender)

# ===== ===== ===== ===== =====
# >>> 함수 이름: joinM
# >>> 함수 기능: 회원 가입시 필수 정보, 선택 정보, 기본 정보를 입력바고 출력
# >>> 매개변수: num1, num2
# >>> 함수 결과: 없음.
# ===== ===== ===== ===== =====

def joinM1(id, pw, *options, gender = '남', loc = "내국인"):
    print("id: {id}, pw: {pw}, gender: {gender}")

def joinM2(*options, id, pw,  gender = '남', loc = "내국인"):
    print("id: {id}, pw: {pw}, gender: {gender}")

# >>> 가변인자 뒤에 나오는 매개변수들은 반드시 변수명 = 데이터
joinM1("AAA", "A1234", "영화보기", "대구", gender = '여', loc = "외국인")

joinM2("AAA", "A1234", "영화보기", "대구", id = "BBB", pw = "B1234", gender = '여', loc = "외국인")

# >>> 권장 매개변수 순서: 일반 매개변수 -> 가변매개변수 -> default 매개변수
# >>> 가변매개변수/키워드 가변매개변수 뒤에 나오는 매개변수에 데이터 설정 시 반드시 매개변수명 = 데이터 형식이어야 한다.

