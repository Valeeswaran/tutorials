import math
from string import ascii_lowercase

get_letter = {index: letter for index, letter in enumerate(ascii_lowercase, start=1)}

def design(num):
    nnums = [i for i in range(1, num + 1)]
    rnums = [i for i in range(1, num+1)]
    rnums.reverse()

    lst =[]
    m = 0
    for i in rnums:
        slst = []
        for j in rnums:
            if i < j:
                if len(slst) == 0:
                    slst.append(j)
                else:
                    slst.append(j)
                    slst.insert(0, j)
        if len(slst)>0:
            lst.append(slst)

    print(lst)
    exit()

    mid = [i for i in rnums] + [j for j in nnums[1:]]
    m = len(mid)
    lst.append(mid)
    r = lst[:-1]
    r.reverse()
    lst = lst[:-1] + [lst[-1]] + r

    padding = []
    for l in lst:
        spad = ""
        for k in l:
            if spad == "":
                spad = "-" + get_letter[k] + "-"
            else:
                spad += get_letter[k] + "-"
        padding.append(spad)

    m = m+m-1
    i = 1
    for p in padding:
        #print('{:-^5}'.format(p))
        if i == len(nnums):
            print(p[1:-1])
        else:
            print('{num:-^{width}}'.format(num=p, width=m))
        i += 1

if __name__ == '__main__':
    n = 3
    design(n)