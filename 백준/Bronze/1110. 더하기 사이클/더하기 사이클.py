str_num = input()
int_num = int(str_num)

add = 0
count = 0

def answer(str_num, count):
    while True:
        add = int(str_num[0]) + int(str_num[1])
        add = str(add)
        str_num = str_num[-1] + add[-1]
        count += 1
        if str(int_num) == str_num:
            print(count)
            break

if int_num == 0:
    print(1)
elif int_num < 10:
    str_num += '0'
    int_num = int(str_num)
    answer(str_num, count)
    
else:
    answer(str_num, count)