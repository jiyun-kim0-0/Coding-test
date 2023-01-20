#min 함수 이용함.
n, m = map(int, input().split())


result = 0

#data 받기
for i in range(n):
    data = list(map(int, input().split())) #data - list
    
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    
    # 가장 작은 수 가운데 가장 큰 수 찾기
    result = max(result, min_value)
    
    
print(result)

    
    