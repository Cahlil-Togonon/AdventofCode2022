with open('input_day1.txt','r') as f:
    calories = f.read().split('\n')

elfs = [[]]
i = 0
for val in calories:
    if val:
        elfs[i].append(int(val))
    else:
        i += 1
        elfs.append([])

total = []
for elf in elfs:
    total.append(sum(elf))

total.sort()
print(total)
answer = total[-1] + total[-2] +total[-3]

print(answer)
