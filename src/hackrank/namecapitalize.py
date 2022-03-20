import re

def solve(s):
    name = re.split(r'(\s+)', s)
    #name = map(str, s.split())
    cap = ""
    skip = False
    for n in name:

        if n[0:1].isupper() or type(n[0:1]) == "int":
           skip = True

        if cap == "":
            if skip == False:
                cap = n.capitalize()
            else:
                cap = n
        else:
            if skip == False:
                cap = cap + n.capitalize()
            else:
                cap = cap + n

        skip = False

    print(cap)

if __name__ == '__main__':
    solve("hello   world  lol valee 23df Bhuvana")
