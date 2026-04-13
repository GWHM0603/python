# >>> str 전용 매서드

# >>> str 원소/요소의 인덱스 반환 -> find(문자/문자열)
# >>> L 인덱스 출력
# >>>  Lu의 인덱스 출력

msg = "Good Luck"
idx1 = msg.find("L")
print(f"L의 인덱스: {idx1}")

idx2 = msg.find(" Lu")
print(f"Lu의 인덱스: {idx2}")
print()

idx3 = msg.find(" lu") # >>> 대소문자 구분 확실히 해야함. 존재하지 않으면 -1 반환. 존재하면 0 이상 인덱스 반환
print(f"lu의 인덱스: {idx3}")
print()


# >>> lower() 모두 소문자로 변경, upper() 모두 대문자로 변경. -> 원본은 수정되지 않음.

new_msg1 = msg.upper()
print(f"msg: {msg}   new_mssg: {new_msg1}")

new_msg2 = msg.lower()
print(f"msg: {msg}   new_mssg: {new_msg2}")

# >>> swap() -> 소문자를 대문자로, 대문자를 소문자로 변경

new_msg3 = msg.swapcase()
print(f"msg: {msg}   new_mssg: {new_msg3}")
print()

# >>> 원소/요소 검사 관련 메서드 -> isXXXX()
# >>> True/Flase
# >>> 알파벳으로 된 str인지 isalpha()
# >>> 숫자만으로 이루어진  str인지 isdecimal()
# >>> 숫자, 알파벳으로 이루어진 str인지 isalphnum()

msg = "Happy"
phone = "01012345678"
user_id = "k1234" 


print(f"{msg}.isalpha() : {msg.isalpha()}")
print(f"{phone}.isalpha() : {phone.isalpha()}")
print(f"{user_id}.isalpha() : {user_id.isalpha()}")
print()

print(f"{msg}.isdecimal() : {msg.isdecimal()}")
print(f"{phone}.isdecimal() : {phone.isdecimal()}")
print(f"{user_id}.isdecimal() : {user_id.isdecimal()}")
print()

print(f"{msg}.isalnum() : {msg.isalnum()}")
print(f"{phone}.isalnum() : {phone.isalnum()}")
print(f"{user_id}.isalnum() : {user_id.isalnum()}")
print()


# >>> 원소/요소 검사 관련 메서드 -> isXXXX()
# >>> True/Flase
# >>> 모든 원소가 대문자인지 isupper()
# >>> 모든 원소가 소문자인지 islower()
# >>> 공백인지 isspace()
# >>> 첫 문자가 대문자인지, 나머진 소문자 istitle()

msg1 = "Good"
msg2 = "HAPPY"
msg3 = "    "

print(f"{msg1}.isupper() : {msg1.isupper()}")
print(f"{msg2}.isupper() : {msg2.isupper()}")
print(f"{msg3}.isupper() : {msg3.isupper()}")
print()

print(f"{msg1}.islower() : {msg1.islower()}")
print(f"{msg2}.islower() : {msg2.islower()}")
print(f"{msg3}.islower() : {msg3.islower()}")
print()

print(f"{msg1}.isspace() : {msg1.isspace()}")
print(f"{msg2}.isspace() : {msg2.isspace()}")
print(f"{msg3}.isspace() : {msg3.isspace()}")
print()

print(f"{msg1}.istitle() : {msg1.istitle()}")
print(f"{msg2}.istitle() : {msg2.istitle()}")
print(f"{msg3}.istitle() : {msg3.istitle()}")
print()
