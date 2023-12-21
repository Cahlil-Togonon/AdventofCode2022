with open("input2.txt","r") as f:
    moves = f.read().split('\n')

def move_rope(rope,j):
    if j >= 10: return

    if (rope[j-1][0] != rope[j][0] and abs(rope[j-1][1]-rope[j][1]) == 2) or (rope[j-1][1] != rope[j][1] and abs(rope[j-1][0]-rope[j][0]) == 2):
        rope[j][0] += 1 if rope[j-1][0]-rope[j][0] > 0 else -1
        rope[j][1] += 1 if rope[j-1][1]-rope[j][1] > 0 else -1
    elif rope[j-1][0] == rope[j][0] and abs(rope[j-1][1]-rope[j][1]) == 2:
        rope[j][1] += 1 if rope[j-1][1]-rope[j][1] > 0 else -1
    elif rope[j-1][1] == rope[j][1] and abs(rope[j-1][0]-rope[j][0]) == 2:
        rope[j][0] += 1 if rope[j-1][0]-rope[j][0] > 0 else -1
    
    move_rope(rope,j+1)

rope = [[0,0] for _ in range(10)]
seen = {(rope[9][0],rope[9][1]):True}
for move in moves:
    if not move: continue
    move = move.split(' ')
    i = int(move[1])
    while i > 0:
        if move[0] == 'U':
            rope[0][0] += 1
        elif move[0] == 'D':
            rope[0][0] -= 1
        elif move[0] == 'R':
            rope[0][1] += 1
        elif move[0] == 'L':
            rope[0][1] -= 1
        move_rope(rope,1)
        seen[(rope[9][0],rope[9][1])] = True
        i -= 1

print(seen.keys())
print(len(seen))
