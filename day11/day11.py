with open("input2.txt","r") as f:
    data = f.read().split('\n')

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = [None,None]
        self.test_div = None
        self.action = [None,None]

    def __str__(self):
        return f"{self.items},{self.operation},{self.test_div},{self.action}"

num_monkeys = round(len(data)/7)
monkeys = [Monkey() for _ in range(num_monkeys)]

for i in range(len(data)):
    j = i // 7
    k = i % 7
    data[i] = data[i].split(' ')
    if k == 1:
        for val in data[i]:
            val = val.split(',')[0]
            if val.isnumeric():
                monkeys[j].items.append(int(val))
    elif k == 2:
        monkeys[j].operation[0] = data[i][-2]
        monkeys[j].operation[1] = data[i][-1]
    elif k == 3:
        monkeys[j].test_div = int(data[i][-1])
    elif k == 4:
        monkeys[j].action[0] = int(data[i][-1])
    elif k == 5:
        monkeys[j].action[1] = int(data[i][-1])
    
round = 1
inspections = [0 for _ in range(num_monkeys)]
while round <= 20:
    for i in range(num_monkeys):
        inspections[i] += len(monkeys[i].items)
        while len(monkeys[i].items):
            item = monkeys[i].items.pop(0)
            
            if monkeys[i].operation[0] == '+':
                item += item if monkeys[i].operation[1] == 'old' else int(monkeys[i].operation[1])
            elif monkeys[i].operation[0] == '-':
                item -= item if monkeys[i].operation[1] == 'old' else int(monkeys[i].operation[1])
            elif monkeys[i].operation[0] == '*':
                item *= item if monkeys[i].operation[1] == 'old' else int(monkeys[i].operation[1])
            elif monkeys[i].operation[0] == '/':
                item /= item if monkeys[i].operation[1] == 'old' else int(monkeys[i].operation[1])
            
            item = item // 3
            if item % monkeys[i].test_div:
                monkeys[monkeys[i].action[1]].items.append(item)
            else:
                monkeys[monkeys[i].action[0]].items.append(item)
    round += 1

print(inspections)
inspections.sort()
print(inspections[-1]*inspections[-2])
