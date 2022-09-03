array = [7,5,9,0,3,1,6,2,4,8] #리스트(배열) 정의 

for i in range (len(array)):
     min_index = i #가장 작은 원소 인덱스(맨 앞에 있는 값 넣음)

     for j in range(i+1,len(array)):
          if array[min_index] > array[j]: #만약 더 작은 원소가 있다면, 대입함.
               min_index = j
     array[i] , array[min_index] = array[min_index] , array[i] # swap 함수 사용
#들여쓰기 위치에 주의함

print(array)
