s = input()
slist=[s[:1], s[1:2], s[2:3]]
cnt = 0
for item in slist:
    if int(item) == 1:
        cnt += 1
print(cnt)