rating = [4, 3, 5, 4, 3]
rcount = len(rating)

#ones = len(rating)
#twos = len([j for j in range(len(rating), 0, -2)])


def getcount(count, array, step, group):

    if count >= step:
        while count >= step:
            group += 1
            if len(array)>0:
                #print(array)
                for i in range(step):
                    array.pop(i)

            count -=step

            getcount(count, array, step, group)
    return group

rats = 0
rats += getcount(rcount, rating, 1, 0)
rats += len([j for j in range(len(rating), 0, -2)])
print(len([j for j in range(len(rating), 0, -2)]))
#rats += getcount(rcount, rating, 1, 0)
print(rats)

#print(getcount(rcount, rating, 3, 0))
#print(getcount(rcount, rating, 2, 0))
#print(getcount(rcount, rating, 3))


