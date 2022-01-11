
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(words[0][-1])
print(words[1][0])
print(words[0][-1]) #역순 -1

def solution (n,words):
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] or len(words[i])==1:
                return [(i%n)+1, (i//n)+1]
            #첫번째 단어는 틀릴 수 없음 world[0][-1] # 비교할 때 공식 주의
            #[:end] 처음부터 end-1 오프셋(인덱스)까지 #딱 직전 인덱스까지 중복있나 체크함
            #한글자 단어 허용안됨
            # 번호- i를 n으로 나눈 나머지+1 
            # 차례- i를 n으로 나눈 몫+1 
    #else 위치 주의 들여쓰기 위치에 따라 완전히 다른 값이 나옴
    else:
        return [0,0]

print(solution(3,words))