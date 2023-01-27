import sys, heapq

case = int(sys.stdin.readline())
stack = []

for i in range(case):
    num = int(sys.stdin.readline())
    if num == 0:
        if stack:
            print(stack[0][1])
            heapq.heappop(stack)
        else:
            print(0)
        
    else:
        # if num in stack:
        #     print('hi')
        #     continue
        # else:
        heapq.heappush(stack, (abs(num), num))

    
