with open('input_day3.txt','r') as f:
    rucksacks = f.read().split()

answer = 0
for rucksack in rucksacks:
    seen = {}
    for i in rucksack[:len(rucksack)//2]:
        seen[i] = True

    for i in rucksack[len(rucksack)//2:]:
        if seen.get(i,False):
            if i.isupper(): answer += 26
            answer += ord(i.lower()) - 96
            break
            
print(answer)