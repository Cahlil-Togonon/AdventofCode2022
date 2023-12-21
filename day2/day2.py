with open('input_day2.txt','r') as f:
    strats = f.read().split('\n')

score = 0
decrypt = {"A":1,"X":1,"B":2,"Y":2,"C":3,"Z":3}
for strat in strats:
    if not strat: continue
    a,b = strat.split(' ')
    a,b = decrypt[a], decrypt[b]

    score += b

    if a == b: score += 3
    else:
        if b == 1 and a == 3: score += 6
        elif a == 1 and b == 3: pass
        elif b > a: score += 6

print(score)