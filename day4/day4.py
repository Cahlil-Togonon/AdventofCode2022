with open('input_day4.txt','r') as f:
    pairs = f.read().split('\n')

answer = 0
with open('output_day4.txt','w') as f:
    for pair in pairs:
        if not pair: continue
        elf1,elf2 = pair.split(',')
        a,b = [int(i) for i in elf1.split('-')]
        c,d = [int(i) for i in elf2.split('-')]
        if (a >= c and a <= d and b >= c and b <= d) or (c >= a and c <= b and d >= a and d <= b):
            f.writelines("1\n")
            answer += 1
        else:
            f.writelines("0\n")

print(answer)