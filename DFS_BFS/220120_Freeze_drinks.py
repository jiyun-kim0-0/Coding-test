#dfs 함수
#특정 노드 방문 / 연결된 모든 노드 방문함.
def dfs(x,y):
    
    #주어진 범위 벗어나면 종료함 # N 행 M 열 ?
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False #종료
    
    #현재 노드 아직 방문 X라면
    if graph[x][y] == 0:
        
        graph[x][y] = 1 #노드 방문처리
        #상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#세로 길이 N(행), 가로 길이 M(열)을 공백으로 기준으로 구분하여 입력받음
n, m = map(int,input().split())

#리스트를 이용하여 맵 정보 입력 받기
graph = [] #리스트
for i in range(n): 
    graph.append(list(map(int,input()))) #공백없이 N번 한줄씩 입력 받음 
    
    #list(map(int,input().split())) 공백 o
    
#모든 노드(각 위치)에 대해 음료수 채움
result =0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True: #방문처리가 되었다면
            result +=1 #count
print(result)