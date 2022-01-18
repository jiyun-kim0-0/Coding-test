#팩토리얼 구현 예제 

#반복문 이용
def factorial_iterative(n):
    
    result=1 #결과값 초기값 정의
    
    for i in range(1,n+1):
        result *= i # ==> result = result * i 
    return result # 결과값 반환

#재귀 함수를 이용
def factorial_resursive(n):
    # n이 1 이하인 경우 1을 반환함. 0!=1 / 1!=1
    if n <= 1:
        return 1
    
    return n * factorial_resursive(n-1)


print('반복문 이용한 팩토리얼의 값 5! : ', factorial_iterative(5))
print('재귀 함수를 이용한 팩토리얼의 값 5! : ', factorial_resursive(5))
    