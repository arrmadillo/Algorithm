import sys


dot = int(sys.stdin.readline()) #컴퓨터 개수
line = int(sys.stdin.readline()) #연결 선


graph = [[] for _ in range(dot+1)]
for i in range(line):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * len(graph)
visited[1] = True #1부터 시작이니깐
stack = [1]
answer = []

while stack:
    cur = stack.pop()

    for num in graph[cur]:
        if not visited[num]:
            visited[num] = True
            stack.append(num)
            answer.append(num)

print(len(answer))
