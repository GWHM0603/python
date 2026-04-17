# ===== ===== ===== ===== =====
# >>> 반복가능한 타입의 원소에 인덱스를 제공해주는 내장함수
# >>> enumnerate()
# >>> for문에서 요소/원소 인덱스가 필요한 경우에 사용함
# ===== ===== ===== ===== =====

datas = ["Good", 2026, "Happy", "좋은 날"]

# >>> 형식 확인하기 isinstance()
print(isinstance(2026, str))
print(isinstance(2026, int)) 


# >>> 기본
for i in range(len(datas)):
    if not isinstance(datas[i], str):
        datas[i] = str(datas[i])
print(datas)


# >>> enumerate() 사용하기
for index_num, i in enumerate(datas):
    if not isinstance(i, str):
        datas[index_num] = str(i)
print(datas)