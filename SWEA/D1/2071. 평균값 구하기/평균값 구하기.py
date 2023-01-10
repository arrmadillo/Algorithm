case = int(input())

for i in range(1, case+1):
    nums = list(map(int, input().split()))
    sum_list = sum(nums)
    print(f'#{i} {round(sum_list/(len(nums)))}')
