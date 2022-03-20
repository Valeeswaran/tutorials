# Replace all ______ with rjust, ljust or center.
# thickness = int(input()) #This must be an odd number
import math

thickness = 5
c = 'H'

# Top Cone
for i in range(thickness):
    # print(str((c*i).______(thickness-1)+c+(c*i).______(thickness-1)))
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    # print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
    print((c * thickness).rjust(thickness + (math.floor(thickness / 2))) + " ".center(thickness * 3) +(c * thickness).ljust(thickness * 4))


# Middle Belt
for i in range((thickness+1)//2):
    # print(" " * 2 + (c * (thickness - (math.floor(thickness / 2))) * 7) + c)
    # print(" " * 2 + (c * (thickness - (math.floor(thickness / 2))) * 7) + c)
    #print(math.floor(thickness / 2))
    #  + (c * (thickness - 1))
    print(" " * math.floor(thickness / 2) + (c * thickness * 5))



# Bottom Pillars
for i in range(thickness+1):
    # print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
    # print((c * thickness).rjust(thickness + (math.floor(thickness / 2))) + " ".center(thickness * math.ceil(thickness / 2)) + (c * thickness).ljust(thickness * 6))
    print((c * thickness).rjust(thickness + (math.floor(thickness / 2))) + " ".center(thickness * 3) + (c * thickness).ljust(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))