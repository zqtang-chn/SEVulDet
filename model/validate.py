from collections import Counter

c = Counter()

file = open("array_slices_va2.txt")
for line in file.readlines():
    line = line.rstrip('\n')
    parts = line.split(',')
    if parts[1] == ' pred:0':
        c.update([parts[0]])
file.close()
mc = c.most_common()
print(mc)
