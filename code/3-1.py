
#동전으로 손님에게 줄 때 최소 개수로 주기

n = int(input('금액을 입력하세요'))
count = 0 

#큰 단위의 화폐부터 확인함.
type = [500,100,50,10]

for coin in type:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 // 연산 - 몫
    n %= coin # n = n % coin 나머지 값을 대입한다. n을 coin으로 나누고 그 나머지값
    
print(count)
    
     