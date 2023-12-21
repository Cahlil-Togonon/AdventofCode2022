with open("input2.txt",'r') as f:
    instructions = f.read().split('\n')

def update_cycle(cycle,X,sig_str):
    cycle += 1
    if cycle % 40 == 20:
        sig_str += cycle * X
    return cycle,X,sig_str

cycle = 0
X = 1
sig_str = 0
for instr in instructions:
    if not instr: continue

    instr = instr.split(' ')
    if instr[0] == "noop":
        cycle,X,sig_str = update_cycle(cycle,X,sig_str)
    elif instr[0] == "addx":
        cycle,X,sig_str = update_cycle(cycle,X,sig_str)
        cycle,X,sig_str = update_cycle(cycle,X,sig_str)
        X += int(instr[1])

print(sig_str)