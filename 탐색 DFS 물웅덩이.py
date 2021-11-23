# 물 웅덩이 수 구하기, 얼음 얼려 먹기

# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력
# 3
# 첫 번쨰 줄에 땅 크기 N, M 1<=N, M<=100
# 두 번째 줄에 N+1번째 줄까지 땅에 대한 표시이다.
# 0은 물 구덩이, 1은 밟아도 무너지지 않는 땅이다.
# 전체 땅 속에서 물 구덩이 개수를 출력한다.

# 5 5
# 00110    ===> [0,0,1,1,0]
# 00010
# 11111
# 00001
# 11100
# 3
# graph는 인접리스트로 노드를 표현한 것
graph = [  # 0번은 사용안 안함
    [],             # 인접행렬
    [2, 3, 8],      # 01100001
    [1, 7],         # 10000010
    [1, 4, 5],      # 10011000
    [3, 5],         # 00101000
    [3, 4],         # 00110000
    [7],            # 00000010
    [2, 6, 8],      # 01000101
    [1, 7],         # 10000010
]
visited = [0] * 9 # [0, 0, 0, 0, 0, 0, 0, 0, 0]
dfs(1) # 1번 노드부터 출발

n,m = map(int, input().split())
graph = []  # 빈 리스트 선언, 빈 배열 선언
for i in range(n):
    graph.append(list(map(int,input())))


def puddle(x,y):
    if x <= 1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 0, 0
        graph[x][y] = 1
        puddle(x - 1, y)   # puddle(-1, 0)
        puddle(x, y - 1)   # puddle(0, -1)
        puddle(x + 1, y)   # puddle(1, 0)
        puddle(x, y + 1)   # puddle(0, 1)
        return True
    else :
        return False


cnt = 0 #물웅덩이 개수
for i in range(n):
    for j in range(m):
        if puddle(i,j) == True:
            cnt += 1
print(cnt)

def dfs(v):
    visited[v] = True # 리스트에 방문했음을 True로 표기
    print(v, end = ' ')
    for i in graph[v]:
        if not visite[i]:
            dfs(i)