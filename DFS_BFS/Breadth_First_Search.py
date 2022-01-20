#최단거리 문제 해결에 사용한다.
#너비 우선 탐색
#큐 이용
from collections import deque

#BFS 메서드 정의
def bfs(graph,start,visited):
    
    queue = deque([start]) #deque 라이브러리
    
    visited[start] = True #현재 노드 방문처리
    
    #큐가 빌때까지 반복함
    while queue:
        v=queue.popleft() #큐에서 하나의 원소 뽑아서 출력함 #popleft 원소 제거시 사용하는 메서드
    



# 2차원 연결 리스트를 이용해 각 노드에 연결된 정보를 표현함.
graph = [
    [], #인덱스 0 는 비워둔다.
    [2,3,8], #1번 노드와 연결된 노드들을 표시함
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 1차원 리스트를 이용해 각 노드가 방문된 정보를 표현
visited = [False] * 9 # False로 정보 초기화 # 노드 1~8 (인덱스 0을 포함해서 * 9)
