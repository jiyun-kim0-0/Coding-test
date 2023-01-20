
#숫자 카드 게임
# p98

#n, m 공백으로 구분하여 입력받기
n, m = map(int,input().split())


result =0

#한 줄씩 받아 확인함.
for i in range(n):
    #데이터 받고
    data = list(map(int,input().split()))
    
    #가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
        
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
#최종 답안 출력
print(result)
    
     
    