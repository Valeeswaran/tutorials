import numpy

''''
print(numpy.identity(3))      # 3 is for  dimension 3 X 3
print(numpy.eye(8, 7, k=1))   # 8 X 7 Dimensional array with first upper diagonal 1.
'''
numpy.set_printoptions(legacy='1.13')

def process(line):
    dimns = numpy.array(line, int)
    # dimns = tuple(dimns)
    print(numpy.eye(dimns[0], dimns[1], k=0))


if __name__ == "__main__":
    line = input().strip().split()
    process(line)