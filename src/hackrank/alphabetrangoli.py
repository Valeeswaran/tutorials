import math
from string import ascii_lowercase

get_letter = {index: letter for index, letter in enumerate(ascii_lowercase, start=1)}

def design(num):
    width = ((num - 1) * 2)

    rnums = [i for i in range(1, num+1)]
    rnums.reverse()
    dnums = {idx+1: num for idx, num in enumerate(rnums)}

    i = len(rnums)

    lst = []
    for n in rnums:
        chars = []
        for c in rnums:
            if i < c:
                if len(chars) == 0:
                    chars.append(c)
                else:
                    chars.append(c)
                    chars.insert(0, c)
            if i == c:

                print(chars.append(c))
                chars.insert(0, c)
        i -=1
        lst.append(chars)
    r = lst[:-1]
    r.reverse()
    lst = lst[:-1] + [lst[-1]] + r
    print(lst)

"""
    i = 1
    for sublst in lst:
        padding = ""
        c = math.floor(len(lst)/2)+1
        # print("length", c+1)

        for l in sublst:
            padding = padding + "-" + get_letter[l] + "-"

        if i == c:
            padding = padding[:-1]
            padding = padding[1:]

        print(padding, "\n")
        i +=1

"""





        #print(("-" * width) + letters[i] + ("-" * width))

"""
    for row in range(n):

        if i < mid:
            if i > 1:
                pc += 2
                dc = cols - (pc * 3)
            print(("-" * math.floor(dc / 2)) + (".|." * pc) + ("-" * math.floor(dc / 2)))

        if i == mid:
            print(("-" * int((cols-7)/2)) + ("WELCOME") + ("-" * int((cols-7)/2)))


        if i > mid:
            if i > mid+1:
                dc = cols - (pc * 3)
            print(("-" * math.floor(dc / 2)) + (".|." * pc) + ("-" * math.floor(dc / 2)))
            pc -= 2
        i += 1
"""

if __name__ == '__main__':
    n = 3
    design(n)