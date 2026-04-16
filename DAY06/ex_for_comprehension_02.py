# ===== ===== ===== ===== =====
# >>> for comprehension -> set
# ===== ===== ===== ===== =====

org_set = {1, 2, 3, 4, 5, 6, 7, 8}
new_set = set()
# 1번 코드
for num in org_set:
    # 2번 코드
    if not num % 2:

        # 3번 코드
        if num >= 6: 
            new_set.add("큰 수")
        else:
            new_set.add(num)

print(new_set, "\n")

org_set = {1, 2, 3, 4, 5, 6, 7, 8}
new_set = {"큰 수" if num >= 6 else num for num in org_set if not num % 2}
#          -------3번 코드------------- -----1번 코드 ----- ----2번 코드---   
print(new_set, "\n")

# >>> 리스트의 원소 값이 짝수면 2를 곱하고, 홀수면 3을 곱해서 저장
new_set = {num * 3 if num % 2 else num *2 for num in org_set}
print(new_set, "\n")



# >>> 리스트의 원소 값이 짝수인 원소만 추가하고
# >>> 그 값이 6미만이면 "작은 수"로 저장
# >>> 그 값이 6 이상이면 "큰 수"로 저장
new_set = {"큰 수" if num >= 6  else "작은 수" for num in org_set if not num % 2}
print(new_set, "\n")
