from copy import deepcopy

with open("input2.txt","r") as f:
    trees = f.read().split('\n')

tree_grid = []
for i in range(len(trees)):
    tree_grid.append([])
    for j in trees[i]:
        tree_grid[i].append(int(j))

seen = [[0]*(len(tree_grid[0])) for _ in range(len(tree_grid))]
i,j = 0,0
while i < len(tree_grid):
    j = 0
    while j < len(tree_grid[0]):
        if i == 0 or i == len(tree_grid)-1 or j == 0 or j == len(tree_grid[0])-1: seen[i][j] = 1 
        j += 1
    i += 1

i,j = 1,1
up = deepcopy(tree_grid)
left = deepcopy(tree_grid)
while i < len(tree_grid) - 1:
    j = 1
    while j < len(tree_grid[0]) - 1:
        if tree_grid[i][j] > up[i-1][j]:
            seen[i][j] = 1
            up[i][j] = tree_grid[i][j] 
        else:
            up[i][j] = up[i-1][j]

        if tree_grid[i][j] > left[i][j-1]:
            seen[i][j] = 1
            left[i][j] = tree_grid[i][j] 
        else:
            left[i][j] = left[i][j-1]
        j += 1
    i += 1

i,j = len(tree_grid) - 2, len(tree_grid[0]) - 2
down = deepcopy(tree_grid)
right = deepcopy(tree_grid)
while i > 0:
    j = len(tree_grid[0]) - 2
    while j > 0:
        if tree_grid[i][j] > down[i+1][j]:
            seen[i][j] = 1
            down[i][j] = tree_grid[i][j] 
        else:
            down[i][j] = down[i+1][j]

        if tree_grid[i][j] > right[i][j+1]:
            seen[i][j] = 1
            right[i][j] = tree_grid[i][j] 
        else:
            right[i][j] = right[i][j+1]
        j -= 1
    i -= 1

score = 0
for row in seen:
    score += sum(row)
print(score)

#############

highest = 0
i,j = 1,1
while i < len(tree_grid) - 1:
    j = 1
    while j < len(tree_grid[0]) - 1:
        left,right,up,down = 1,1,1,1
        while tree_grid[i][j-left] < tree_grid[i][j] and j-left-1 >= 0: left += 1
        while tree_grid[i][j+right] < tree_grid[i][j] and j+right+1 < len(tree_grid[0]): right += 1
        while tree_grid[i-up][j] < tree_grid[i][j] and i-up-1 >= 0: up += 1
        while tree_grid[i+down][j] < tree_grid[i][j] and i+down+1 < len(tree_grid): down += 1
        highest = max(highest,left*right*up*down)
        j += 1
    i += 1
print(highest)