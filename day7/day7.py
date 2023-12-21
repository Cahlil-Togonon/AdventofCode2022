with open("input.txt","r") as f:
    cmds = f.read().split('\n')

class Directory:
    def __init__(self,parent):
        self.files = {}
        self.parent = parent
        self.size = 0
    def calc_size(self,dir_sizes):
        for file in self.files.values():
            if type(file) is int:
                self.size += file
            else:
                self.size += file.calc_size(dir_sizes)
        dir_sizes.append(self.size)
        return self.size

root = {"/":Directory(None)}
wd = root["/"]
for cmd in cmds:
    cmd = cmd.split(' ')
    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "/":
                wd = root["/"]
            elif cmd[2] == "..":
                wd = wd.parent
            else:
                wd = wd.files[cmd[2]]
    elif cmd[0] == "dir":
        wd.files[cmd[1]] = Directory(wd)
    else:
        wd.files[cmd[1]] = int(cmd[0])

dir_sizes = []
root["/"].calc_size(dir_sizes)
print(dir_sizes)

answer = 0
for dir_size in dir_sizes:
    if dir_size <= 100_000:
        answer += dir_size
print(answer)

total_space = root["/"].size
space_to_clear = 30_000_000 - (70_000_000 - total_space)
print(space_to_clear)
dir_sizes.sort()

for dir_size in dir_sizes:
    if dir_size >= space_to_clear:
        print(dir_size)
        break