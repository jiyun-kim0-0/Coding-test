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

#위 두가지 방법의 경우 다소 효율성이 떨어짐

"""
#세번째 방법
from queue import Queue

que = Queue()

#데이터 넣기
que.put(1)
print(que)

que.put(2)
print(que)

que.put(3)
print(que)

#데이터 삭제
que.get()
print(que)

que.get()
print(que)

que.get()
print(que) """

from collections import deque
#deque 라이브러리 이용 (덱)
#list 자료형 이용시 시간복잡도가 높아짐.

queue = deque([7, 8, 9])
print(queue)

queue.append(10)
print(queue)

#제거시 popleft 메서드 이용
queue.popleft()
print(queue)

print(queue) #먼저 들어온 순서대로 출력함.
queue.reverse() #역순
print(queue)

