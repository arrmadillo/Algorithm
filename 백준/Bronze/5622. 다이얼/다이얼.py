import sys

text = list(sys.stdin.readline().rstrip())

alphabet = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6,
         'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
time = 0

for i in text:
    for k, v in alphabet.items():
        if i in k:
            time += v
print(time)

