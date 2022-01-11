
arr = [5,6,3,2,7,1]

#start - index 0 / end - len(arr)-1 - last index
def quick_sort(arr,start,end):
    
    if start >= end: #원소의 개수가 1개이면 종료함
        return
    
    pivot = start # 첫번째 요소가 피봇이 됨
    left = start +1 # 피봇보다 1 큰 index
    right = end # 마지막 요소 index
    
    while (left <= right):
        #피봇보다 큰 데이터
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1 # index
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)
    return arr


print(quick_sort(arr, 0, len(arr) - 1))