import re

def paint(p, n):
    color_map = {
        'A': 'RYB', 
        'O': 'RY', 
        'P': 'RB', 
        'G': 'YB', 
        'R': 'R', 
        'Y': 'Y', 
        'B': 'B',
        'U': 'U'
    }
    
    stroke = 0
    for target in 'RYBU':
        cur = ''
        for color in p:
            if target in color_map[color]:
                cur += target
            else:
                cur += ' '
        cur_norm = cur.strip()
        if len(cur_norm) > 0 and target != 'U':
            stroke += len(re.split(' +', cur_norm))
    return stroke

T = int(input())
for i in range(T):
    N = int(input())
    P = input()
    result = paint(P, N)
    print(f'Case #{i+1}: {result}')
 
