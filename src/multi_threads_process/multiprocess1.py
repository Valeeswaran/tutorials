import time
import multiprocessing


def calc_square(numbers):
    print("calculate square numbers")
    for num in numbers:
        print("square", num * num)


def calc_cube(numbers):
    print("calculating cubes")
    for num in numbers:
        print("cube", num * num * num)


# Note if you are not using the following line then you will get an error message since the functions are not
# initialised.
if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("completed!")
