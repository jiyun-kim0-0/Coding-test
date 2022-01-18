
stack=[]  #list 자료형 이용
#push
stack.append(2)
stack.append(4)
stack.append(6)

print("stack:",stack)

stack_char = []
stack_char.append('가')
stack_char.append('나')
stack_char.append('다')

#pop
stack.pop()
print('후입선출 pop-1 :',stack)

stack.pop()
print('후입선출 pop-2 :',stack)

stack.pop()
print('후입선출 pop-3 :',stack)

stack.append(3)
stack.append(2)
stack.append(1)
print("append 함수 이용 요소 넣기: ",stack)
print(stack[::-1]) #최상단 원소부터 출력 #리스트 뒤집어서 출력함(먼저 나가고자 하는 원소부터 출력)
print(stack) #최하단 원소부터 출력 #먼저 들어온 요소부터 출력

print("stack_char:",stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
