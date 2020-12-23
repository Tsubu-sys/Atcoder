n=int(input())
nlist = list(map(int,input().split()))
cnt = 0

def isEven(tarlist, n):
    i = 0
    for i in range(n):
        if tarlist[i] % 2 == 1:
            return 0
    return 1

while isEven(nlist, n) == 1:
    for i in range(n):
        nlist[i] = nlist[i] / 2
    cnt += 1
print(str(cnt))
