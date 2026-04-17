## =================================================
## 함수의 매개변수/파라미터 
##
## -> 함수 코드 실행 시에 필요판 데이터를 전달 받는 변수
## -> 함수마다 개수가 다름 또는 없는 경우도 있음
#
## =================================================
## 함수기능 : 학생의 학점을 출력해주는 기능. 학생마다 과목개수와 과목이 다름
## 함수이름 : get_grade
## 매개변수 : **score
## 함수결과 : grade
## =================================================

def get_grade(**score): # 딕셔너리로 받음
    # print("키워드 파라미터: ", type(score), "\n")
    grade = 0
    for num in score.values():
        grade += num 
    
    avg = (grade / len(score)) if len(score) else 0
    
    return avg

def addInt(*nums): # 튜플로 받음
    return sum(nums)

data = [11, 22, 33, 44, 55]
print(addInt(*data)) # addInt(11, 22, 33, 44, 55)와 같은 의미로서 *변수명으로 하면 언패킹하여 전달하는것임. 단, 컨테이너 타입만 가능.

datas = {"sci":89, "art": 80, "dance": 77}

print(get_grade(**datas), "\n") # 언패킹해서 전달

