# >>> str과 산술연산자
# >>> +: str + str => str 연결
# >>> *: str * int => str을 정수만큼 반복 연결

# >>> str 생성

msg = "Good Luck"
year = "2026!!"
msg_year = msg + " " + year
print(msg_year)
print()

msg_int = (msg + " ") * 3
print(msg_int)
print()

# >>> str과 멤버연산자
print(f"G in msg: {'G' in msg}")
print(f"g in msg: {'g' in msg}")
print(f"Goo in msg: {'Goo' in msg}")
print()
