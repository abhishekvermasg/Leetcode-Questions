d = {}
l1 = ""
l2 = ""

for i in req:
    if i.startswith("# "):
        l1 = i[1:].strip().replace("\n", "")
        d[l1] = {}
    if i.startswith("## "):
        l2 = i[2:].strip().replace("\n", "")
        d[l1][l2] = []
    if i[0].isdigit():
        d[l1][l2].append(i)

ds = {}
for i in d.keys():
    cnt = 0
    temp = []
    for j in d[i].keys():
        for k in d[i][j]:
            if k not in temp:
                temp.append(k)
            cnt += 1
    ds[i] = list(temp)
    print(f"{i}\nOld Count: {cnt}\nNew Count: {len(list(temp))}")

for i in ds:
    print(i)
    print()
    for j in ds[i]:
        print(j.replace('\n', ''))
    print()
    print()
