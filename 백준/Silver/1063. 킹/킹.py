import sys

moving = {'R':(0,1), 'L':(0,-1), 'B':(1,0), 'T':(-1,0), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}

alpha = [i for i in 'ABCDEFGH']

king, stone, T = sys.stdin.readline().rstrip().split()
T = int(T)

#좌표
king_x = 8-int(king[-1])
king_y = alpha.index(king[0])
stone_x = 8-int(stone[-1])
stone_y = alpha.index(stone[0])

for _ in range(T):
     command = sys.stdin.readline().rstrip()
     command = moving[command] # 좌표 
     
     king_x += command[0]
     king_y += command[-1]
     
     if not(0 <= king_x < 8 and 0 <= king_y < 8): #범위 벗어나면
          
          king_x -= command[0]
          king_y -= command[-1]       
          continue
     if king_x == stone_x and king_y == stone_y: #위치 같으면
          stone_x += command[0]
          stone_y += command[-1]
          
          
          if not(0 <= stone_x < 8 and 0 <= stone_y < 8):
               stone_x -= command[0]
               stone_y -= command[-1]
               
               king_x -= command[0]
               king_y -= command[-1] 
               
print(alpha[king_y], 8-king_x, sep='')
print(alpha[stone_y], 8-stone_x, sep='')
