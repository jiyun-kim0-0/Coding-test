
#세로 길이 N(행), 가로 길이 M(열)을 공백으로 기준으로 구분하여 입력받음
n , m = map(int,input().split())

#리스트를 이용하여 맵 정보 입력 받기
graph = [] #리스트
for i in range(n):
    graph.append(list(map(int,input())))
    
#모든 노드(각 위치)에 대해 음료수 채움
result =0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1
            
#dfs 함수 정의
def dfs(x,y):
    
    return False
