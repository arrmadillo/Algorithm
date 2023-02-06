import sys

text = sys.stdin.readline().rstrip()

happy = text.count(':-)')
sad = text.count(':-(')

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')




