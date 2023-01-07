hour, min = map(int, input().split())

if min - 45 < 0:
    if hour == 0:
        print(f'23 {60 - (45 - min)}')
    else:
        print(f'{hour - 1} {60 - (45 - min)}')
else:
    print(f'{hour} {min - 45}')