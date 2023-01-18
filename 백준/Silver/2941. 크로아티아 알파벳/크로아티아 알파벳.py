import sys

a = sys.stdin.readline().rstrip()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
just = 0

for i in alphabet:
    if a.find(i) != -1:
        count += 1
        a = a.replace(i, ",") 
    
print(len(a))
    

