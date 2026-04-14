# >>> 특정 문자열/문자로 시작하는지 또는 끝나는지 검사하는 메소드
# startswith(문자열/문자) : 시작 검사  -> True/False 반환
# endwith(문자열/문자)    : 끝 검사 -> True/False 반환 

filename1 = "data.csv"
filename2 = "image.jpg"
filename3 = "image.png"

# >>> 언패킹: 원소 개수만큼 변수명을 선언해서 저장하는 것.
# >>>        컨테이너 자료형에서 1개의 변수명으로 관리하던 데이터를 여러 개의 변수명으로 나누어서 저장
filename1, filename2, filename3 = "data.csv", "image.jpg", "image.png"

# >>> 특정 문자열/문자로 시작하는지 검사 진행 : startwith()
ret = filename1.startswith('i')
print(f"{filename1} -> {ret}\n")

ret = filename1.startswith("ima")
print(f"{filename1} -> {ret}\n")

ret = filename1.startswith("d")
print(f"{filename1} -> {ret}\n")


# >>> 특정 문자열/문자로 끝나는지 검사 진행 : endwith()
ret = filename2.endswith("sv")
print(f"{filename1} -> {ret}\n")

ret = filename2.endswith(("sv", "jpg", "png")) # 튜플로 입력하여 OR 역할을 해줌
print(f"{filename1} -> {ret}\n")


