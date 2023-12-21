with open("input2.txt",'r') as f:
    grid = f.read().split('\n')

def DFS(grid,seen,depth,i,j,ei,ej,answer):
    if (i,j) == (ei,ej):
        answer[0] = min(depth,answer[0])
        return

    seen[(i,j)] = True
    if i > 0 and not seen.get((i-1,j),False) and ord(grid[i-1][j])-ord(grid[i][j]) <= 1:
        DFS(grid,seen,depth+1,i-1,j,ei,ej,answer)
    if i < len(grid)-1 and not seen.get((i+1,j),False) and ord(grid[i+1][j])-ord(grid[i][j]) <= 1:
        DFS(grid,seen,depth+1,i+1,j,ei,ej,answer)
    if j > 0 and not seen.get((i,j-1),False) and ord(grid[i][j-1])-ord(grid[i][j]) <= 1:
        DFS(grid,seen,depth+1,i,j-1,ei,ej,answer)
    if j < len(grid[0])-1 and not seen.get((i,j+1),False) and ord(grid[i][j+1])-ord(grid[i][j]) <= 1:
        DFS(grid,seen,depth+1,i,j+1,ei,ej,answer)
    seen[(i,j)] = False
    return

for i in range(len(grid)):
    if grid[i].find('S') != -1:
        si = i
        sj = grid[i].find('S')
        grid[si] = grid[si].replace('S','a')
    if grid[i].find('E') != -1:
        ei = i
        ej = grid[i].find('E')
        grid[ei] = grid[ei].replace('E','z')
    
seen = {}
answer = [len(grid)*len(grid[0])]
DFS(grid,seen,0,si,sj,ei,ej,answer)
print(answer)