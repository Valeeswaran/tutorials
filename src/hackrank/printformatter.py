def print_formatted(number):
    xl = len(str(number))
    yl = len(str(oct(number)).replace("0o", ""))
    zl = len(str(hex(number)).replace("0x", ""))
    bl = len(str(bin(number)).replace("0b", ""))
    #print(number, str(bin(number)).replace("0b", ""), bl)

    for n in range(1, number+1):
        x = str(n).rjust(bl)
        y = str(oct(n)).replace("0o", "").rjust(bl)
        z = str(hex(n)).replace("0x", "").upper().rjust(bl)
        b = str(bin(n)).replace("0b", "").rjust(bl)

        print(x + " " + y + " " + z + " " + b)

if __name__ == '__main__':
    number = 63
    print_formatted(number)