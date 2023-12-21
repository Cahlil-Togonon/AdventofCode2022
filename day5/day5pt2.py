with open('input_day5.txt','r') as f:
    steps = f.read().split('\n')

i = 0
for step in steps:
    if step[1].isnumeric():
        break
    i += 1

num_crates = int(steps[i][-2]) 

crates = [[] for _ in range(num_crates)]
j = i - 1
while j >= 0:
    for k in range(num_crates):
        if steps[j][k*4+1] != ' ':
            crates[k].append(steps[j][k*4+1])
    j -= 1

print(crates)

i += 2
while i < len(steps):
    if not steps[i]: break
    step = steps[i].split(' ')
    num,src,dest = int(step[1]),int(step[3]),int(step[5])
    temp = []
    for _ in range(num):
        temp.append(crates[src-1].pop())
    for _ in range(num):
        crates[dest-1].append(temp.pop())
    i += 1

print(crates)

answer = ""
for crate in crates:
    if len(crate):
        answer += crate[-1]
    else:
        answer += ' '

print(answer)