with open("input2.txt","r") as f:
    moves = f.read().split('\n')

def move_rope(H,T,direction):
    if direction == 'U':
        H[0] += 1
    elif direction == 'D':
        H[0] -= 1
    elif direction == 'R':
        H[1] += 1
    elif direction == 'L':
        H[1] -= 1
    
    if (H[0] != T[0] and abs(H[1]-T[1]) == 2) or (H[1] != T[1] and abs(H[0]-T[0]) == 2):
        T[0] += 1 if H[0]-T[0] > 0 else -1
        T[1] += 1 if H[1]-T[1] > 0 else -1
    elif H[0] == T[0] and abs(H[1]-T[1]) == 2:
        T[1] += 1 if H[1]-T[1] > 0 else -1
    elif H[1] == T[1] and abs(H[0]-T[0]) == 2:
        T[0] += 1 if H[0]-T[0] > 0 else -1

H = [0,0]
T = [0,0]
seen = {(T[0],T[1]):True}
for move in moves:
    if not move: continue
    move = move.split(' ')
    i = int(move[1])
    while i > 0:
        move_rope(H,T,move[0])
        seen[(T[0],T[1])] = True
        i -= 1

print(seen.keys())
print(len(seen))