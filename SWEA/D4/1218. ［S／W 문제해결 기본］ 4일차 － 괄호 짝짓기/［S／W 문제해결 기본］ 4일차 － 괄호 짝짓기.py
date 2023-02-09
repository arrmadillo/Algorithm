
answer = []
for _ in range(1, 11):
    case = input()
    signs = list(input())
    sign_dic = {'(':0, '[':0, '{':0, '<':0}
    for sign in signs:
        if -1 in sign_dic.values():
            print(f'#{_} 0')
            break
        elif sign in sign_dic:
            sign_dic[sign] += 1
        else:
            if sign == ')':
                sign_dic['('] -= 1
            elif sign == ']':
                sign_dic['['] -= 1
            elif sign == '}':
                sign_dic['{'] -= 1
            else:
                sign_dic['<'] -= 1
    else:
        print(f'#{_} 1')
         
print(answer)       
            
            

