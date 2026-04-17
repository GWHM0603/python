# ===== ===== ===== ===== =====
# >>> Iterable 타입: 반복이 가능한 데이터 타입
# >>> for in  반복문으로 요소 추출 가능한 타입들
# >>> 확인: 메서드에 __iter__() 존재 유무
# ===== ===== ===== ===== =====

iterator = [10, 20,  30].__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print()


it = iter([1, 2, 3])
print(next(it)) # 1을 'Pop'해서 보여줌
print(next(it)) # 2를 'Pop'해서 보여줌

# 이제 it 안에는 3만 남았습니다.
for i in it: 
    print(i)    # 3만 출력되고 끝남

# 한 번 더 돌리면?
for i in it: 
    print(i)    # 아무것도 출력되지 않음 (텅 비었음)
print(list(it))
print()

nums = [4, 7, -1, 3, 5]

new_iterator = iter(nums)
print(next(new_iterator), "\n")
print(nums)
print(next(new_iterator), "\n")
print(nums)
print(next(new_iterator), "\n")
print(nums)