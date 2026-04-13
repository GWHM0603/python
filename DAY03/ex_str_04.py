# >>> 원소/요소 변경 후 반환 -> replace(이전문자/이전문자열, 새로운문자/새로운문자열)
# >>> 변환된 새로운 str 반환
# >>> 원본 str 변경 안됨
# >>> 인덱스 기반 원소값 변경 지원안함. 

# "good luck" -> "Good Luck"

msg = "good luck"

new_msg = msg.replace("g", "G")
print(f"msg -> {msg}    new_msg -> {new_msg}")
print()
 
msg = "good luck good luck good luck"
# >>> 해당되는 모든 문자/문자열은 변경됨
new_msg = msg.replace("g", "G")
print(f"msg -> {msg}    new_msg -> {new_msg}")
print()

# >>> replace(이전문자/이전문자열, 새로운문자/새로운문자열, 변경할 개수)
new_msg = msg.replace("g", "G", 1)
print(f"msg -> {msg}    new_msg -> {new_msg}")
print()


# >>> 1개의 str을 여러 개의 str로 분리: split()
# >>> 메서드 사용시 분리 기준 문자/문자열 설정 가능
# >>> 리스트에 여러 개 분리된 str 담아서 반환

data = "Happy New Year 2026"
# >>> [기본] 공백문자 기준으로 분리
ret = data.split()
print(f"data: {data}    {type(data)}    {len(data)}개")
print(f"ret: {ret}    {type(ret)}    {len(ret)}개")
print()

# >>> [기본] 문자 기준으로 분리
ret = data.split("-")
print(f"data: {data}    {type(data)}    {len(data)}개")
print(f"ret: {ret}    {type(ret)}    {len(ret)}개")
print()

# >>> 여러 개의 str을 1개 str로 연결: join()
# >>> [설정] 연결 문자 지정 필요

ret = data.split() # 분리된 상태
new_data = "___".join(ret)
print(ret, end=" ")
print(f"// new_data: {new_data}    {type(new_data)}    {len(new_data)}개")
print()


# ch9, ch22, 