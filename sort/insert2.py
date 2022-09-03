array = [7,5,9,0,3,1,6,2,4,8] #리스트(배열) 정의 

for i in range (1,len(array)):
     for j in range (i,0,-1): # 시작 위치,마지막 위치,간격
          # 인덱스 i부터 1까지 1씩 감소하며 반복함.
          # 마지막 위치의 원소는 포함하지 x

          #더 큰 값이 왼쪽에 위치한 경우
          if array[j] < array[j-1]:
               array[j] , array[j-1] = array[j-1], array[j] #swap
          else: #자신보다 왼쪽 데이터의 값이 작을 경우 멈춤.
               break
print(array)

