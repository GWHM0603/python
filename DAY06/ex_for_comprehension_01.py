# ===== ===== ===== ===== =====
# >>> for comprehension -> list
# ===== ===== ===== ===== =====


# >>> 형식 1: 반복문으로 컨테이너 자료형 생성
# >>> [원소 for 원소 in 반복가능한 자료형]

org_list = [1, 2, 3]
new_list = []

for num in org_list:
    new_list.append(num * 3)
print(new_list, "\n")


# ----- ----- ----- ----- -----

# >>> 리스트 컴프리헨션
new_list = [num * 3 for num in org_list]
print(new_list, "\n")


# ===== ===== ===== ===== =====

# >>> 형식 2: 반복문으로 컨테이너 자료형 생성
# >>> [원소 for 원소 in 반복가능한 자료형 if 조건식]

org_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []

for num in org_list:
    if not num % 2:
        new_list.append(num * 3)
print(new_list, "\n")


# ----- ----- ----- ----- -----

# >>> 리스트 컴프리헨션
new_list = [num * 3 for num in org_list if not num % 2] 
print(new_list, "\n")


# ===== ===== ===== ===== =====

# >>> 형식 3: 반복문으로 컨테이너 자료형 생성
# >>> [원소 if 조건 else 원소 for 원소 in 반복가능한 자료형]

org_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []

for num in org_list:
    if not num % 2:
        new_list.append(num * 3)
    else:
        new_list.append(num)
        
print(new_list, "\n")


# ----- ----- ----- ----- -----

# >>> 리스트 컴프리헨션
new_list = new_list.append(num * 3 if not num % 2 else num)
print(new_list, "\n")


# >>>  [원소 if 조건 else 원소 for 원소 in 반복가능한 자료형 if 조건식]
# >>>  -----원소 표현 결정 --- -----원소 추출 ------------ --필터링--
# >>> 짝수 값을 가진 원소만 사용. 
# >>> 짝수 값이 10이상이면 큰 수로 저장, 미만이면 그대로 저장

org_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []

for num in org_list:

    if not num % 2:

        if num >= 6: 
            new_list.append("큰 수")
        else:
            new_list.append(num)
        
print(new_list, "\n")

org_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = ["큰 수" if num >= 6 else num for num in org_list if not num % 2] 
print(new_list, "\n")