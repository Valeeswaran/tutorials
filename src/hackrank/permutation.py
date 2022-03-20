
def permutation(nums):
    if len(nums) <= 1:
        yield nums
    else:
        for perm in permutation(nums[1:]):
            for i in range(len(perm)+1):
                # nb str[0:1] works in both string and list contexts
                yield perm[:i] + nums[0:1] + perm[i:]


if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    #print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
    #print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n])
    x = 1
    y = 1
    z = 2

    nums = [x, y, z]
    for i in permutation(nums):
        print(i)


