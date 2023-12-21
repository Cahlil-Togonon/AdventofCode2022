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

highest = 0
for elf in elfs:
    total = sum(elf)
    highest = max(total,highest)

print(highest)
