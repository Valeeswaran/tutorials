import math
from string import ascii_lowercase

get_letter = {index: letter for index, letter in enumerate(ascii_lowercase, start=1)}

def print_rangoli(n):
    onums = [i for i in range(1, n+1)]
    rnums = [i for i in range(1, n+1)]
    rnums.reverse()

    x =0
    lst =[]
    m = 0
    for i in rnums:
        slst = []
        for j in rnums:
            if i <= j:
                slst.append(j)
        if x > 0:
            rlst = slst[:-1]
            rlst.reverse()
            slst = slst + rlst
        x +=1
        lst.append(slst)
        r = lst[:-1]
        r.reverse()
    lst = lst[:-1] + [lst[-1]] + r
    #print(lst)

    padding = []
    m = len(onums)

    x =1
    for l in lst:
        spad = ""
        for k in l:
            if spad == "":
                spad = "-" + get_letter[k] + "-"
            else:
                spad += get_letter[k] + "-"
        if x == m:
            m = len(spad[1:-1])
        padding.append(spad)
        x += 1


    i = 1



    for p in padding:
        #print('{:-^5}'.format(p))
        if i == len(onums):
            print(p[1:-1])
        else:
            print('{num:-^{width}}'.format(num=p, width=m))
            #print(p, m)
        i += 1

if __name__ == '__main__':
    n = 10
    print_rangoli(n)