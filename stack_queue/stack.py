
stack=[]

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

print("stack_char:",stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
print('후입선출 pop : ',stack_char.pop()+ ' stack_char :',stack_char)
