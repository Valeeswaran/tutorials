import numpy

array_1 = numpy.array([1, 2, 3])
array_2 = numpy.array([4, 5, 6])
array_3 = numpy.array([7, 8, 9])

#print(numpy.concatenate((array_1, array_2, array_3)))

array_1 = numpy.array([[1, 2, 3], [0, 0, 0]])
array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])

#print(numpy.concatenate((array_1, array_2), axis=0))

def process(dimns, lines):
    dimns = numpy.array(dimns, int)
    rows = dimns[:-1]
    cols = dimns[-1]

    array = []
    for line in lines:
        array.append(line)
    array = numpy.array(array, int)
    print (array)



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

    process(dimns, lines)
