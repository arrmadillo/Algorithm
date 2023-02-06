import sys


dot = int(sys.stdin.readline()) #컴퓨터 개수
lines = int(sys.stdin.readline()) #연결 선

graph = [[] for _ in range(dot + 1)] # n번 컴퓨터와 연결된 컴퓨터들 
visited = [False] * (dot + 1)

for _ in range(lines):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited[1] = True

while stack:
    cur = stack.pop()

    for num in graph[cur]:
        if not visited[num]:
            visited[num] = True
            stack.append(num)

print(visited.count(True)-1) #컴퓨터1은 제외 (1 때문에 감염된 바이러스 컴퓨터의 수를 구하기 위해)    
