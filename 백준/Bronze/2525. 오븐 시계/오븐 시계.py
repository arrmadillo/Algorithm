hour, min = map(int, input().split())
time = int(input())

if min + time > 59:
    hour += (min + time) // 60
    min = (min + time) % 60
    if hour >= 24:
        hour -= 24 
else:
    min += time

print(f'{hour} {min}')