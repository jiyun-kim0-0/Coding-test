#가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
#작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.

from array import array


price = 1260
count = 0

#화폐 단위
#큰 단위부터 차례대로 확인 list
array = [500,100,50,10]

for coin in array:
    count += price//coin #동전개수 #나머지의 몫
    price %= coin # n = n % coin 나눗셈 결과의 나머지
    
print(count)
