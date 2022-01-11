arr = [5,6,3,2]
#my_list = list(map(int,input().split()))

def selection(arr):
    for i in range(len(arr)-1): # i는 arr 의 길이 - 1 까지 돌 수 있음
        min = i # 일단 무작위로 최소 인덱스 지정
        for j in range (i+1,len(arr)):
            # i=0 / (0,4) 끝 숫자는 포함되지 않는다 0 ~ 3
            # i=1 / (2,4)
            # i=2 / (3,4)
            # 
            
            if arr[j]<arr[min]:
                min = j # 최솟값 변경
        arr[i] , arr[min] = arr[min] , arr[i] #값 변경
    return arr
    

print(selection(arr))

        
        