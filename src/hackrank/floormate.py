import math

def design(rows, cols):
    mid = math.ceil(rows / 2)

    i = 1
    c1 = 1
    c2 = 0
    pc = 1
    dc = cols - 3
    for row in range(rows):

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


if __name__ == '__main__':
    n, m = 7, 21
    n, m = 11, 33
    n, m = map(int, input().split())
    design(n, m)