#재귀 제한 존재 in python
#의도적으로 무한 루프를 만들려고 하는 것이 아니라면, 종료 조건 명시함

def recursive_function(i):
    
    if i == 100: # 재귀 제한 조건 100번째 호출했을 때 종료됨
        return
    #break는 해당 if문만 종료시키지만, return은 해당 메소드가 호출된 곳까지 종료시킴.
    #즉 if문을 포함한 메소드 자체를 종료함
    #return문이 함수의 실행을 중단하기 위해 쓰인다면, break문은 반복문의 실행을 중단하기 위해 쓰인다.
    
    print(i, '번째 재귀함수에서 ', i+1 ,'번째 재귀함수를 호출함')
    
    #마치 스택과 같다. stack 짐 쌓기 후입선출
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료함')
    
    
recursive_function(1)