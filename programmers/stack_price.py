
prices = [1,2,3,2,3]

def solution(prices):
    
    answer = [0]*len(prices)
    stack=[0]
    
    for i in range(1,len(prices)): # 1 ~ len(p)-1
        if prices[i] < prices[stack[-1]]: #
            for j in stack[::-1]: #값이 정해지지 않은 시점 역순 탐색
                if prices[i] < prices[j]: #j 값이 더 큼.
                    answer[j] = i-j # 가격이 떨어지지 않는 시간 저장
                    stack.remove[j] #값이 정해지면, stack 에서 제거됨.
                else:
                    break #for 문에서 빠져나감
        stack.append(i)
    for i in range(0,len(stack)-1):
        answer[stack[i]] = len(prices) - stack[i] -1
    return answer