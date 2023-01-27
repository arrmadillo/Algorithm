import sys, heapq

heap = list(map(int, sys.stdin.readline().split()))

heapq.heapify(heap) # 정렬

heapq.heappop(heap) # 가장 작은 값 삭제 -> 두번째로 작은값이 부모로 변경

print(heap[0]) 