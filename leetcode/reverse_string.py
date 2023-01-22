#문자열 뒤집기
#입력값 - 문자배열 / 리턴없이 리스트 내부 직접 조작함

from ast import List
from turtle import left, right


#포인터를 이용한 swqp
#매개변수로 리스트 받음.
def reverseString_pointer(self,s: List[str]) -> None:
    left,right =0,len(s)-1 #?..
    
    while left < right:
        s[left] , s[right] = s[right] , s[left]
        #리스트의 값을 바꾼다.
        left += 1 #다음 원소
        right -= 1 #오른쪽에서 왼쪽으로 다음 원소
        

def reverseString_method(self,s: List[str]) -> None:
    #리턴값 X
    s.reverse()
    
    