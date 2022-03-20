import numpy

numpy.set_printoptions(legacy='1.13')
if __name__ == "__main__":
    array = input().strip().split(" ")
    array = numpy.array(array, float)

    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))