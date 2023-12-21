with open("input2.txt",'r') as f:
    inputs = f.read().split('\n')

grid = []
i,j = 0,0
while i < len(inputs):
    j = 0
    grid.append([])
    while j < len(inputs[i]):
        if inputs[i][j] == 'S':
            si,sj = i,j
            grid[i].append(0)
        elif inputs[i][j] == 'E':
            ei,ej = i,j
            grid[i].append(25)
        else:
            grid[i].append(ord(inputs[i][j])-97)
        j += 1
    i += 1
    
BFS = [(si,sj,0)]
seen = {(si,sj):True}
while len(BFS):
    node = BFS.pop(0)
    i,j,depth = node[0],node[1],node[2]
    if (i,j) == (ei,ej):
        print(depth)
        break

    if i > 0 and not seen.get((i-1,j),False) and grid[i-1][j]-grid[i][j] <= 1:
        seen[(i-1,j)] = True
        BFS.append((i-1,j,depth+1))
    if i < len(grid)-1 and not seen.get((i+1,j),False) and grid[i+1][j]-grid[i][j] <= 1:
        seen[(i+1,j)] = True
        BFS.append((i+1,j,depth+1))
    if j > 0 and not seen.get((i,j-1),False) and grid[i][j-1]-grid[i][j] <= 1:
        seen[(i,j-1)] = True
        BFS.append((i,j-1,depth+1))
    if j < len(grid[0])-1 and not seen.get((i,j+1),False) and grid[i][j+1]-grid[i][j] <= 1:
        seen[(i,j+1)] = True
        BFS.append((i,j+1,depth+1))