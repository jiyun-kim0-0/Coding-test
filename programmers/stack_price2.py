
prices = [1,2,3,2,3]

print(prices[::-1]) #역순

#answer = [0]*len(prices)
#print(answer)

from collections import deque
 
def solution(prices):
    
    answer = []
    prices = deque(prices) #큐
    print(prices)
    
    while prices: #배열 모두 탐색->  []
        c = prices.popleft() # 배열의 첫번째 요소 저장 (prices에서 첫번째 요소 remove)
        print(prices)
        count = 0
        
        for i in prices:  # 다른 배열 요소와의 비교
            if c > i: # 감소 case
                count += 1 # count+=1 하고 중단
                break
            count += 1 # 아니면 count+=1 늘리며 계속 탐색

        answer.append(count)
    return answer

print(solution(prices))
    