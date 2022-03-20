import textwrap


def wrap(string, max_width):
    print(textwrap.fill(string, width=max_width))


if __name__ == '__main__':
    str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    wdt = 4
    str = input()
    wdt = int(input())
    wrap(str, wdt)