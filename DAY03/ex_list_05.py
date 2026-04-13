## =======================================
## 컨테이너 자료형 - [1] List
## List 전용 메서드 사용
## =======================================

# >>> 1 ~ 30 범위에서 7의 배수로만 구성된 데이터

num_list = range(7,31,7) # 타입이 range임 -> 형 변환 필요
num_list = list(num_list)
print(f"[1] 리스트: {num_list}    개수: {len(num_list)}개")
print()

# >>> List 전용 함수 즉, 메서드 사용
# >>> 원소/요소 추가 -> 마지막: 변수명.appned()

num_list.append(100)
print(f"[2] 리스트: {num_list}    개수: {len(num_list)}개")
print()


# >>> 객체명.insert(a, b) a번째 위치에 B 삽입
num_list.insert(0, 90)
print(f"[3] 리스트: {num_list}    개수: {len(num_list)}개")
print()

num_list.insert(-1, 1000)
print(f"[4] 리스트: {num_list}    개수: {len(num_list)}개")
print()

print("=====================================================")
str_list = ['a', 'e', 'c', 'd','f', 'b']
str_list.sort()
print(f"[1]{str_list}")
print()

str_list.sort(reverse=True)
print(f"[2]{str_list}")
print()

# >>> 단순 뒤집기만 함. 정렬 기능 없음
str_in = ['h', 'e', 'l', 'l' ,'o']
str_in.reverse()
print(str_in)

# >>> List: count vs len
count_list = [1, 1, 1, 2, 2]
print(f"[1] {count_list}    {len(count_list)}개") # 리스트의 길이 반환
print(f"[2] {count_list}    {count_list.count(1)}개") # 해당 값의 개수 반환, 없으면 0으로 반환해줌.
print()

# >>> 원소/요소 삭제 : remove vs pop
int_list = [1, 2, 3, 4, 5]
int_list.remove(3)
print("==== remove(x): x 요소 삭제 ====")
print(f"[1] {int_list}")
print()

print("==== pop(): 마지막 인덱스에 해당하는 요소 삭제 후 반환 ====")
int_list = [1, 2, 3, 4, 5] 
print(f"[2] {int_list.pop()}") # 마지막 인덱스 추출 반환
print(f"[3] {int_list}")
print()
print(f"[4] {int_list.pop()}") # 마지막 인덱스 추출 반환
print(f"[5] {int_list}")
print()


print("==== pop(인덱스 위치): 특정 인덱스 위치에 있는 요소 삭제 후 반환 ====")
int_list = [1, 2, 3, 4, 5]
print(f"[6] {int_list.pop(2)}") # 특정 인덱스 추출 후 반환
print(f"[7] {int_list}")
print()

# >>> 리스트 원소를 모두 삭제할려면 clear(), 리스트 자체를 삭제할려면 del 사용


# >>> 원소/요소 인덱스 찾기 -> 변수명.index(data)
# >>> 첫 번째로 발견되는 데이터 인덱스 반환
# >>> 존재하지 않으면 error 반환

num_list = [1, 2, 2, 3, 3, 3]
if 1 in num_list:
    print(num_list.index(2))
else:
    print("해당 인덱스는 존재하지 않습니다")

print()

num_list = [1, 2, 2, 3, 3, 3, 2, 2, 1]
idx1 = num_list.index(2) # 첫 번재 2의 인덱스
print(f"[1] {idx1}")
print()

idx2 = num_list.index(2, idx1 + 1) # 두 번째 2의 인덱스
print(f"[2] {idx2}")
print()

idx3 = num_list.index(2, idx2+ 1) # 세 번째 2의 인덱스
print(f"[3] {idx3}")
print()

idx4 = num_list.index(2, idx3+ 1) # 네 번째 2의 인덱스
print(f"[4] {idx4}")
print()

# >>> 원소/요소 개수 증가/확장 -> 변수명.extend(반복타입객체)
# >>> list 원소가 증가
# >>> >>> 반복 가능 타입/Iterable타입: for ~ in 가능한 타입. 인덱스가 있는 타입들이 해당함.

# ->>> num_list.extend(32) 32는 그냥 정수이므로 반복가능한 타입이 아님
num_list.extend([32])
print(num_list)
print()

# >>> append는 마지막 값을 단 1개씩만 추가.
# >>> extend는 itenable 타입이면 여러 개 동시에 추가 가능
num_list.extend([32, 33, 34]) # 리스트 + 리스트, 튜플 + 튜플과 같은 의미 
print(num_list)
print()


num_list.extend("hello") # 문자열(iterable타입)도 가능 
print(num_list)
print()

# >>> str타입은 엄밀하게 말하면 컨테이너 타입...

# >>> 매직코드 or 매직 메서드: Python에 특수한 기능을 부여해 놓은 것들 
# >>> EX: __init__()
