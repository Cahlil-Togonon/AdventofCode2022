from ast import literal_eval
from functools import cmp_to_key

def compare(l,r):
    l = l if isinstance(l,list) else [l]
    r = r if isinstance(r,list) else [r]
    for li,ri in zip(l,r):
        if isinstance(li,list) or isinstance(ri,list):
            ans = compare(li,ri)
        else:
            ans = ri - li
        if ans != 0:
            return ans
    return len(r)-len(l)

with open("input2.txt",'r') as f:
    input = f.read().split('\n')

packets = []
for line in input:
    if line:
        packets.append(literal_eval(line))

i = 0
right_order = []
while i < len(packets):
    if compare(packets[i],packets[i+1]) > 0:
        right_order.append(i//2+1)
    i += 2
print(right_order)
print(sum(right_order))

# PART 2
right_order = sorted(packets+[[[2]]]+[[[6]]], key=cmp_to_key(compare), reverse = True)
idx = [n for n,packet in enumerate(right_order,1) if packet in [[[2]],[[6]]]]
print(idx)
print(idx[0]*idx[1])