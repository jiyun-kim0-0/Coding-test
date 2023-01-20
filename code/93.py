#문제 - n개의 수로 이루어진 배열을 입력받고 m번 만큼 더해서 가장 큰 수를 만든다. 이때, 같은 수의 경우 k번 이상 더할 수 없음.


#공백으로 구분하여 입력을 받는다.
n, m, k = map(int,input().split())

#n개의 수를 공백으로 구분하여 입력 받는다.
data = list(map(int, input().split()))

#입력받은 수 정렬함.
data.sort() 

#작 - 큰 정렬되었음
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수 각각 저장함.

result =0

while True:
    for i in range(k):
        #같은 수는 k번까지 더할 수 있지만
        if m == 0:
            #숫자 더할 수 있는 횟수가 m=0이면 무쓸모
            break #반복문 탈출
        result += first
        m -= 1 #더할 때마다 m -1 을 해준당
        
    #그 다음 k번 다 끝났으면
    #다시 m 몇번 남았는지 확인한다.
    if m == 0:
        break
    
    # 두 번째로 큰 수를 한번 더함.
    result += second
    
    m -= 1
    #더할 때마다 -1 한다
    
    print(result) #최종 답 출력
    
    
    

