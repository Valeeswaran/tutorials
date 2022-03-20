clist = ["orange", "apple apple", "banana anything banana", "mangao"]

cstr = " ".join([c for c in clist])
mlist = list(set([m for m in cstr.split()]))
print(mlist)
clst = []

for m in mlist:
    if m != "anything":
        clst.append(cstr.replace("anything", m))


print(clst)

