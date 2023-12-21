with open('input_day3.txt','r') as f:
    rucksacks = f.read().split()

answer = 0
groups = [[] for _ in range(len(rucksacks)//3)]
for i in range(len(rucksacks)):
    groups[i//3].append(rucksacks[i])

for group in groups:
    seen = {}
    for i in range(len(group)):
        for chr in group[i]:
            seen[chr] = seen.get(chr,0) | (2**i)

    for key in seen:
        if seen[key] == 7:
            if key.isupper(): answer += 26
            answer += ord(key.lower()) - 96
            break

print(answer)