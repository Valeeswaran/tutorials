import numpy

'''
a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
numpy.set_printoptions(legacy='1.13')
'''

numpy.set_printoptions(legacy='1.13')

def print_result(arr, rows=2):
    a = numpy.array([arr])
    print(numpy.tile(a, (rows, 1)))


def calc(a, b, rows):
    a = numpy.array(a, int)
    b = numpy.array(b, int)

    print_result(numpy.add(a, b), rows)
    print_result(numpy.subtract(a, b), rows)
    print_result(numpy.multiply(a, b), rows)
    #print_result(numpy.array(numpy.divide(a, b), int))
    print_result(numpy.array(numpy.floor_divide(a, b)), rows)
    print_result(numpy.mod(a, b), rows)
    print_result(numpy.power(a, b), rows)

def process(dimns, lines):
    dimns = numpy.array(dimns, int)
    rows = dimns[:-1][0]
    cols = dimns[-1]

    array = numpy.array([],int)
    for line in lines:
        array = numpy.append(array, numpy.array(line, int))

    if rows == 1:
        array = array.reshape([2, 4])
    if rows == 2:
        array = array.reshape([cols, cols])

    if rows == 1:
        calc(array[0], array[1], rows)
    elif rows == 2:
        calc(array[0], array[2], 2)


    # for line in lines:
    #     if len(array) == 0:
    #         array = numpy.array(numpy.array(line, int))
    #         array = numpy.expand_dims(array, axis=0)
    #
    #     else:
    #         array = numpy.append(array, line, axis=1)
    #         pass
    #
    #
    #     tmp = numpy.array(line, int)
    #     #array = numpy.append(array, tmp, axis=0)
    #print(array)





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