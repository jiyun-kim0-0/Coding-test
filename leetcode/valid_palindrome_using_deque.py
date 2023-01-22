#자료형 데크 사용
from collections import deque
import collections
from gc import collect
from typing import Deque

#자료형 deque 사용 -> 속도 향상

class test:
    def is_palindrome(slef, s: str) -> bool:
        strs: Deque = collections.deque()
        #매개변수 self
        
        #collections ->
        #타입 어노테이션
        for char in s:
            if char.isalnum(): #영문자/숫자 판별
                strs.append(char.lower()) #low()함수를 통해 모두 다 소문자로 만듬


        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): #맨 앞 부분 문자와 맨 뒷부분의 pop() 같은지 비교함.
                return False
            
            return True

my_string=input("문자열 입력")
my_test = test() #객체 생성
a=my_test.is_palindrome(my_test,my_string)