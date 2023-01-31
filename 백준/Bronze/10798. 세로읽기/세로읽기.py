import sys

words = []
answer = []

for _ in range(5):
    words.append(sys.stdin.readline().rstrip())
    
for word in words: #글자리스트
    for i in range(len(word)): #글자 인덱스
        try:
            answer[i] += word[i]
        except:
            answer.append(word[i])
            
        
print(*answer, sep='')