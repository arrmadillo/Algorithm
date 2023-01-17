T = int(input())
sum_list = []

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    sum_list.append(sum(nums))
print(*sum_list[:T], sep='\n')