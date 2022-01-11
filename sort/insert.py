
a=[3,5,2,1]

def insert_sort(arr):

    for end in range(1,len(a)): # 1 ~ 배열 a의 길이
        insert_key = a[end]
        i=end
        print(end)
        while i>0 and a[i-1] > insert_key:
            a[i] = a[i-1]
            i -= 1 # 1씩 작아진다
        a[i]=insert_key
        
    return a

print(insert_sort(a))