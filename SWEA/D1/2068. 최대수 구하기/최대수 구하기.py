case = int(input())

for i in range(1, case+1):
    nums = list(map(int, input().split()))
    print(f'#{i} {max(nums)}')