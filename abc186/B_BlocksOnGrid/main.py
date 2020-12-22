H, W = map(int, input().split())
P = [input().split() for i in range(H)]

minInts = []
for i in range(H):
    minInts.append(min(P[i]))
# min of all
minInt = int(min(minInts))

deleteCnt = 0
for i in range(H):
    for j in range(W):
        tar = int(P[i][j]) - minInt
        if (int(tar) != 0):
            deleteCnt = deleteCnt + int(P[i][j]) - minInt
print(deleteCnt)