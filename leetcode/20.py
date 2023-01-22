#괄호로 된 입력값이 올바른지 판별하라.
#push / pop - stack

class solution:
    def is_valid(self,s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        #스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char) # 없으면 넣고
                print(char)
                print(stack)
                #조건 not
            elif not stack or table[char] != stack.pop(): #pop 원소 제거
                return False
        return len(stack) == 0 # 스택이 비어있다면
    
s=solution()
print(s.is_valid('(){}[]'))