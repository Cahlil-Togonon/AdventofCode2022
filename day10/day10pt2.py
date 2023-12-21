with open("input2.txt",'r') as f:
    instructions = f.read().split('\n')

def update_cycle(cycle,X,crt):
    cycle += 1
    if abs(X + 1 - (cycle % 40)) <= 1:
        crt += '#'
    else:
        crt += '.'
    if cycle % 40 == 0:
        crt += '\n'
    return cycle,X,crt

cycle = 0
X = 1
crt = ""
for instr in instructions:
    if not instr: continue

    instr = instr.split(' ')
    if instr[0] == "noop":
        cycle,X,crt = update_cycle(cycle,X,crt)
    elif instr[0] == "addx":
        cycle,X,crt = update_cycle(cycle,X,crt)
        cycle,X,crt = update_cycle(cycle,X,crt)
        X += int(instr[1])

print(crt)