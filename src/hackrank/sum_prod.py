import numpy

numpy.set_printoptions(legacy='1.13')
if __name__ == "__main__":
    dimns = []
    lines = []
    count = 0
    while True:
        try:
            if count == 0:
                dimns = input().strip().split(" ")
            else:
                lines.append(input().strip().split(" "))
            count +=1
        except EOFError:
            break

    array = numpy.array(lines, int)
    print(numpy.prod(numpy.sum(array, axis=0)))