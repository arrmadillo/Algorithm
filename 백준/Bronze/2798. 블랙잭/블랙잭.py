n, m = map(int, input().split())

card = list(map(int, input().split()))
max_num = 0

for num1 in range(n):
    for num2 in range(num1+1, n):
        for num3 in range(num2+1, n):
            if card[num1] + card[num2] + card[num3] > m:
                continue
            elif card[num1] + card[num2] + card[num3] > max_num:
                max_num = card[num1] + card[num2] + card[num3]
        
print(max_num)