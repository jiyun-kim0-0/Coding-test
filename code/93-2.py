n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

#num = k+1 #수열의 길이
#a = m / num # 수열이 반복되는 횟수
#b = m % num

# 수열의 길이 k+1
# 수열이 반복되는 횟수 * k => 가장 큰 수가 더해지는 횟수
# 이때 나누어 떨어지지 않는 경우도 고려함.
count = int(m/(k+1)) * k
count += m % (k+1) #나머지

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #남은 수만큼 곱한다.

print(result)

