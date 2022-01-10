
#list / map을 통해서 리스트의 요소를 반복문 없이 받을 수 있다.
#num_list = list(map(int, input().split()))
#print(num_list)

a=[2,10,1,5]

def merge_sort(num_list):
    
    #길이
    if len(num_list) < 2:
        return num_list
    
    mid = len(num_list) // 2 #중간인덱스 저장
    left = merge_sort(num_list[:mid]) #리스트 슬라이싱
    right = merge_sort(num_list[mid:])
    
    sorted = []
    l = r = 0 #기본값 설정
    
    #길이가 0보다 클 때
    while l < len(left) and r < len(right):
        if left[l] < right[r]: #오른쪽이 더 클 때 -정상
            sorted.append(left[l]) #sorted 되었으니 append
            l += 1
            
        else: #왼쪽이 더 클 때
            sorted.append(right[r])
            r +=1
            
    sorted += left[1:] #처음부터 끝까지
    sorted += right[r:]
    
    return sorted

print(merge_sort(a))

#단점 배열 요소에 따라 슬라이싱 중복이 일어날 수 있음.
