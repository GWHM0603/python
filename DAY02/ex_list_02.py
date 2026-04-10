## =================================================
## 컨테이너 자료형 - [순서 있는 자료형] list
## -> 다양한 내장 함수 사용하기
## ==================================================

# 리스트 생성하기
# ---------------------------------------------------

# >>> 기본 리스트 형태
scores_list1 = [90, 89, 100, 79, 99]
scores_list2 = list([90, 89, 100, 79, 99])

print(scores_list1)
print(scores_list2)
print()
print()

# >>> 다양한 데이터를 리스트에 저장하기
data1 = []
data2 = ["Hi", 123, 0.98, False]
data3 = [[100, 200, 300], [1, 2, 3, 4, 5]]

# >>> 내장함수: type(변수명) -> 저장 데이터의 타입 확인
print(f"type(data1):    {type(data1)}          {data1}")
print(f"type(data2):    {type(data2)}          {data2}")
print(f"type(data3):    {type(data3)}          {data3}")
print()
print()

# >>> 내장함수: len(변수명) -> 데이터/요소 개수 반환 함수
print(f"len(data1):    {len(data1)}          {data1}")
print(f"len(data2):    {len(data2)}          {data2}")
print(f"len(data3):    {len(data3)}          {data3}")
print()
print()

# >>> 내장함수: max(변수명) -> 데이터/요소 중 최고값 데이터 찾기
# >>> 내장함수: min(변수명) -> 데이터/요소 중 최소값 데이터 찾기
data4 = [23, 123, -3, 0.98, 99.999]
data5 = ["Abc", "APPle", "anaconda", "zoo"] 

# > 제일 앞 문자를 아스키 코드 기준으로 비교. 앞 글자가 같으면 다음 글자 비교함
# > str 데이터는 문자 1개 1개의 코드값을 비교함.

print(f"max(data4):    {max(data4)}     min(data4):    {min(data4)}")
print(f"max(data5):    {max(data5)}     min(data5):    {min(data5)}")
print()
print()

# >>> 내장함수: sum(변수명) -> 데이터/요소들의 합계 반환 함수
# >>> sum 함수는 수치 데이터만 가능함.
print(f"sum(data1):    {sum(data1)}          {data1}")
print(f"sum(data4):    {sum(data4)}          {data4}")
print()
print()
