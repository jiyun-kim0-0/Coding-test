score = int(input("점수를 입력하시오"))


while(score<=100):

    if 90<=score:
        print("A")
        break
    elif 80<=score:
        print("B")
        break
    elif 70<=score:
        print("C")
        break
    elif 60<=score:
        print("D")
        break
    else:
        print("F")
        break
