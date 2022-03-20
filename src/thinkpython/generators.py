# For memory better memory management
# Generators allow you to create a function that returns one item at a time rather than all the items at once.
# This means that if you have a large dataset, you don’t have to wait for the entire dataset to be accessible.

def __iter__(self):
    return self.__generator()

def __generator(self):
    for item in self.items():
        yield  item


# Use built-in functions and libraries
# Use built-in functions and libraries whenever you can. Built-in functions are often implemented using the best
# memory usage practices.
oldlist = ["Valee", "Bhuvana", "RISHIKESWARAN", "Vaishnawi"]
# Don’t do this:
mylist=[]
for myword in oldlist:
      mylist.append(myword.upper())

print(mylist)
# Better choice:
mylist=map(str.lower, oldlist)
print(type(mylist))
for x in mylist:
    print(x)