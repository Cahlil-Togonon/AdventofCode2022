with open('input_day6.txt','r') as f:
    buffers = f.read().split('\n')

for buffer in buffers:
    seen = {}
    start = 0
    end = 13
    for i in range(end):
        seen[buffer[i]] = seen.get(buffer[i],0) + 1

    while end < len(buffer):
        seen[buffer[end]] = seen.get(buffer[end],0) + 1
        
        flag = True
        for val in seen.values():
            if val >= 2:
                flag = False
                break
        
        if flag:
            print(end+1)
            break

        seen[buffer[start]] -= 1
        start += 1
        end += 1