#만들어 질 수 있는 가장 큰 수
#숫자로 이루어진 문자열

data = input("숫자를 입력")
result = int(data[0])

# 0빼고 시작하니까,
for i in range (1,len(data)):
    num = int(data[i])
    
    #두 수 중에 하나라도 0 혹은 1 이라면 곱하기보다 더하기가 유리함.
    if num <= 1 or result <= 1: #문자열의 첫번째 숫자가 0 혹은 1인 경우
        result += num
    else:
        result *= num

print(result)
