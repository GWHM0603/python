# >>> 컨테이너 자료형  - dict
# >>> 형식: {키1:값1, 키2:값2, ...}
# >>> 특징 1: 키와 값의 묶음올 데이터 저장
# >>> 특징 2:키는 중복되면 안되고, 만약 중복시 마지막 값이 저장됨.
# >>> 특징 3: 순서가 없음. 키로 데이터/값을 읽기/추출/선텍 가능하기 때문.

# >>> dict 데이터 생성
# 예시: 6개 과목별 점수 저장

scores_dict = {"국어": 90, "수학": 88, "영어": 87, "화학": 78, "지구과학": 97, "한국사":93}
print(f" 타입: {type(scores_dict)}   원소 개수 {len(scores_dict)}   데이터: {scores_dict}")


# >>> dict 자료형 원소 다루기 
# >>> [1] 원소 읽기: 변수명[키] -> 값
print(scores_dict["지구과학"])

if "물리" in scores_dict:
    print(scores_dict["물리"])
else:
    print("물리 존재하지 않습니다.")
print()

# >>> 데이터 변경: 변수명[키] = 값
scores_dict["체육"] = 89
print(scores_dict)


# >>> 데이터 삭제: del 변수명[키]
del  scores_dict["체육"]

print(scores_dict)