import sys

count = int(sys.stdin.readline())
log = {}
for i in range(count):
    name, state = sys.stdin.readline().rstrip().split()
    if state == 'enter':
        log[name] = state
    else: #leave일 경우 삭제
        del log[name]
print(*sorted(log.keys(), reverse=True), sep='\n')




