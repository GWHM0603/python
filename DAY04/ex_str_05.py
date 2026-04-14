# >>> 문자열 앞 부분과 끝 부분의 공백 제거하는 메서드: strip()
# >>> 문자열 사이의 공백은 제거하지 않음.

msg = "   Good Luck~!!!  " # 앞 공백 3개, 끝 공백 2개
print(f"msg 원소 개수: {len(msg)}개, {msg}\n")

msgall = msg.strip()
print(f"앞과 끝 부분 공백 제거 버전 원소 개수: {len(msgall)}개, {msgall}\n")

msgleft = msg.lstrip()
print(f"앞 부분만 공백 제거 버전 원소 개수: {len(msgleft)}개, {msgleft}\n")

msgright = msg.rstrip()
print(f"뒷 부분만 공백 제거 버전 원소 개수: {len(msgright)}개, {msgright}\n")


data="flower.jpg"
new_data = data.rstrip(".jpg")
print(data, new_data, sep =" ==> ")
      
data="exflower.jpg"
new_data = data.rstrip(".jpg")
new_data = new_data.lstrip("ex")
print(data, new_data, sep =" ==> ")


# >>> str의 끝 부분 즉, 오른쪽에서 왼쪾으로 이동하며 인덱스 찾기 메소드
# >>> rindex() : 끝 -> 앞으로 이동하면서 찾기, 없으면 Error 발생
# >>> rfind() : 끝 -> 앞으로 이동하면서 찾기, 없으면 -1 반환

datas = [3, 1, -2, 8, 3, 1, 1, 3]
datas = "3, 1, -2, 8, 3, 1, 1, 3"

# >>> 데이터 3의 인덱스 찾기. 단, 마지막 3의 인덱스 찾기

idx = datas.index('3')
print(f"첫 번째 3의 인덱스: {idx}\n")
idx = datas.index('3', idx + 1)
print(f"두 번째 3의 인덱스: {idx}\n")
idx = datas.index('3', idx + 1)
print(f"세 번째 3의 인덱스: {idx}\n")

idx = datas.rindex('3')
print(f"세 번째 3의 인덱스: {idx}\n")
