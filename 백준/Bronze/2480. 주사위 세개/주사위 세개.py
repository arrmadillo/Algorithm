nums = list(map(int, input().split()))
max_num = max(nums)
cnt = {}

for i in nums:
    try:
        cnt[i] += 1
    except:
        cnt[i] = 1

if len(cnt) == 3:
    print(max_num * 100)
elif len(cnt) == 2:
    
    for k, v in cnt.items():
        
        if v == 2:
            print(1000+k*100)
else:
    print(10000+max_num*1000)
