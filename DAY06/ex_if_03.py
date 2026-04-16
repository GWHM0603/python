# >>> 나이가 20살 이상이거나 또는 여성인 경우 왼쪽으로 이동하세요.
while True:
    people = input("성별과 나이를 입력하세요: ")


    if len(people):
        gender, age = people.split()

        if  age.isdecimal():
            age = int(age)

            if gender.isalpha():
                if age >= 20 or gender == "여성":
                    print("왼쪽으로 가세요")
                    break
                else:
                    print("오른쪽으로 가세요.")
                    break
            else:
                print("잘못된 데이터입니다.\n")
                

        else:
            print("숫자가 입력되지 않았습니다.\n")

    else:
        print("입력된 데이터가 없습니다.\n")



