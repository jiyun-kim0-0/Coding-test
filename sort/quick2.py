array = [5,7,9,0,3,1,6,2,4,8]

#매개변수 배열, 피벗 인덱스(0),(정렬할 배열의) 마지막 인덱스
def quick_sort(array,start,end):
     if start >= end: #원소가 1개인 경우 종료함.
          return
     pivot = start # 피벗은 첫번째 원소
     left = start + 1
     right = end
# 인덱스
     while(left <= right):
          #피벗보다 큰 데이터를 찾을 때까지 반복함.
          #while 조건 - 피벗보다 작으면 인덱스 +1
          while(left <= end and array[left] <= array[pivot]):
               left += 1

          #피벗보다 작은 데이터를 찾을 때까지 반복함.
          #while 조건 - 피벗보다 크면 인덱스 -1
          while(right > start and array[right] >= array[pivot]):
               right -= 1

# 데이터 교체
          if(left > right): # 엇갈렸다면 작은 데이터와 피벗 교체
               array[right] , array[pivot] = array[pivot] , array[right]
          else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체함.
               array[left] , array[right] = array[right] , array[left]

          quick_sort(array,start,right-1) #피벗 기준 왼쪽 데이터 정렬
          quick_sort(array,right+1,end) # 피벗 기준 오른쪽 데이터 정렬

quick_sort(array,0,len(array)-1)
print(array)
               