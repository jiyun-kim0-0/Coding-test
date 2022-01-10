
arr = [4,2,5,7]

def bubble_sort(arr):
    end = len(arr)-1 #배열의 끝 인덱스 값 저장
    
    while end>0:
        last_swap=0
        
        for i in range(end):
            if arr[i] > arr[i+1]:
                #값이 더 크다면
                arr[i] , arr[i+1] = arr[i+1] , arr[i] #값 바꾸기
                last_swap=i # swap 값 저장 - if 조건 충족
            end = last_swap #
    
    return arr

print(bubble_sort(arr))
