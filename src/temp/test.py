t = 12344

c = 0
for x in range(len(str(t))):
    c += int(str(t)[x])

print(c)
exit()

print(len(str(t)))
length = 0

while t > 0:
    t = t/10
    t = round(t)
    length += 1
print(length)