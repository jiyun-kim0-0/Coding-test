queue = [1,2,3,4,5]

queue.append(6)
queue.append(7)
print(queue)

queue.pop(0) # index 지정
print(queue)

queue.pop(3)
print(queue)
#선입선출
#뒤에서 데이터 추가 and 앞에서 데이터 나감

#다른 방식 insert(데이터 삽입 위치 지정 가능)
#앞에서 데이터 추가 and 뒤에서 데이터 나감
queue_list = [1,2,3]

queue_list.insert(0,4)
print(queue_list)
queue_list.insert(0,5)
print(queue_list)

queue_list.pop()
print(queue_list)

queue_list.pop()
print(queue_list)