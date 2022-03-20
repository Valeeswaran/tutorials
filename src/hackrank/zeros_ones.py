import numpy

''''
print(numpy.zeros((1, 2)))  # Default type is float
print(numpy.zeros((1, 2), dtype=numpy.int64))  # Type changes to int

print(numpy.ones((1, 2)))                     # Default type is float
print(numpy.ones((1, 2), dtype=numpy.int64))  # Type changes to int
'''

def process(line):
    dimns = numpy.array(line, int)
    dimns = tuple(dimns)
    print(numpy.zeros(dimns, dtype=numpy.int64))
    print(numpy.ones(dimns, dtype=numpy.int64))

if __name__ == "__main__":
    line = input().strip().split()
    process(line)