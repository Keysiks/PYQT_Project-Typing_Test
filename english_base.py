with open("russian_base.txt", encoding="utf-8") as f:
    file = f.readlines()
sp = []
for i in file:
    sp.append(i.strip().split()[1])
with open("russian_base.txt", "w", encoding='utf-8') as f:
    for i in sp:
        f.write(i + "\n")