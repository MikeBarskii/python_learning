# https://stepik.org/lesson/24460/step/9?unit=6766

n = int(input())

args = dict()
args['global'] = (set(), set())
for _ in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        args[namesp][0].add(arg)
    if cmd == 'create':
        args[arg][1].add(namesp)
        args[namesp] = (set(), set())
print(args)
