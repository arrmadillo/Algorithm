import sys

text = sys.stdin.readline().rstrip()

grade = {'A':4, 'B':3, 'C':2, 'D':1, '+':0.3, '0':0.0, '-':-0.3}

print(0.0 if text == 'F' else grade[text[0]] + grade[text[1]])

