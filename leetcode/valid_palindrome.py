#회문 여부 판별
#일반적으로 읽었을 때와 거꾸로 읽었을 때 같은 문장을 회문이라고 정의함.


def is_palindrome(s: str) -> bool:
     #타입 어노테이션
     #매개변수 s - str / 함수 리턴값 bool으로 지정함.
     strs = []
     for char in s:
          if char.isalnum(): #영문자/숫자 판별
               strs.append(char.lower()) #low()함수를 통해 모두 다 소문자로 만듬


     while len(strs) > 1:
          if strs.pop(0) != strs.pop(): #맨 앞 부분 문자와 맨 뒷부분의 pop() 같은지 비교함.
               return False

     return True

print(is_palindrome("A man, a plan, a canal: Panama"))