import sys

punch = sys.stdin.readline().rstrip()
punch = punch.split("(^0^)")

print(punch[0].count('@'), punch[1].count('@'))