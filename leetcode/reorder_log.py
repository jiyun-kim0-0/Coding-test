#로그 재정렬문제
#로그의 가장 앞부분은 식별자임
#문자로 구성된 로그가 숫자 로그보다 앞에 위치함
#문자가 동일할 경우, 식별자순
#숫자 로그는 입력 순



def reorderLogfiles(self, logs: list[str]) -> list[str]:
    
    def __init__(self) -> None:
        self.logs = map(str,input("입력").split(','))
        
    letters, digits = [],[] #문자 로그와 숫자 로그로 나눔
    for log in logs:
        #log.split()[1] 인덱스 주의
        if log.split()[1].isdigit: # isdigit() 함수 -> 숫자 여부 판별
            digits.append(log) # 숫자로 변환 가능
        else:
            letters.append(log)
        
        #2개의 키 람다 표현식
        #sort 함수(정렬 기준,후순위 정렬 기준)
        #식별자 제외 문자열 정렬 -> 후순위로 식별자를 기준으로 정렬함
    letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    return letters + digits

