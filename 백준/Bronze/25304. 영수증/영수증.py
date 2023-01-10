sum_price = int(input())
count = int(input())
a = {}
cal = 0

for i in range(count):
    key, value = map(int, input().split())
    if key in a:
        a[key] += value
    else:
        a[key] = value

for k, v in a.items():
    cal += k*v
    
if cal == sum_price:
    print('Yes')
else:
    print('No')