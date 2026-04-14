# >>> dict 내장함수
scores_dict1 = {"국어": 90, "수학": 88, "영어": 87, "화학": 78, "지구과학": 97, "한국사":93}

# >>> max, min -> 키만 비교함. 값은 확인안함.
mx, mn = max(scores_dict1), min(scores_dict1)
print(f"최댓값: {mx}    최솟값: {mn}")

# >>> sorted() 키를 기준으로만 정렬
ret = sorted(scores_dict1)
print(f"정렬 결과: {ret}") # sorted()는 항상 리스트를 반환


