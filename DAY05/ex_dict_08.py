# >>> 딕셔너리 원소/요소 읽어오는 메소드 -> get()
data_dict = {1: 100, 2: 98, 3: 100}
print(f"{len(data_dict)}\n{data_dict}\n")

ret = data_dict.get(2)

print(f"get(2)결과값: {ret}\n")
print(f"{len(data_dict)}\n{data_dict}\n")

# >>> 키 존재하지 않을 경우엔 None 값 반환

# >>> 키 정보만 가지고 딕셔너리 생성 메소드: fromkeys()
key = range(10, 100, 10)
data_dict = dict.fromkeys(key)
print(f"{len(data_dict)}\n{data_dict}\n")

data_dict = dict.fromkeys(key,"*")
print(f"{len(data_dict)}\n{data_dict}\n")
