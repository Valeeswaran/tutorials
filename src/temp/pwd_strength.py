from string import ascii_lowercase

str = "good"
str = "".join([c for c in str if c.lower() in ascii_lowercase and c != c.upper()])
l = len(str)

perm = []
for i in range(l):
    for j in range(l+1):
        if str[i:j] != "":
            perm.append(str[i:j])

strength1 = 0

for k, v in enumerate(perm):
    print(k, len(list(set(v))), v)
    strength1 += len(list(set(v)))

print(perm, strength1)