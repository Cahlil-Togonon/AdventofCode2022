with open('input.txt','r') as f:
    strats = f.read().split('\n')

score = 0
decrypt = {"A":1,"X":0,"B":2,"Y":3,"C":3,"Z":6}
for strat in strats:
    if not strat: continue
    a,b = strat.split(' ')
    a,b = decrypt[a], decrypt[b]

    score += b

    if b == 3: score += a
    else:
        if b == 6 and a == 3: score += 1
        elif b == 0 and a == 1: score += 3
        elif b == 6: score += (a + 1)
        elif b == 0: score += (a - 1)

print(score)