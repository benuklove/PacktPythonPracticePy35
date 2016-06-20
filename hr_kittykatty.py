"""

  Created on 6/19/2016 by Ben


"""


#  Number of test cases, T
#  1 <= T <= 100
def constrain_t():
    t = int(input().strip())
    if t > 100 or t < 1:
        constrain_t()
    return t

T = constrain_t()

i = 0
arr = []
while i < T:
    #  Number of blocks, N
    N = int(input().strip())

    #  do stuff

    #  fill list of "blocks" with numbers
    blocks = []
    for every_block in range(N):
        blocks.append(every_block)
    #  turns = N - 1


    i += 1
    #  Put those sums into the list for stdout
    arr.append(total)

#  Output each sum of even fib numbers on a new line
for j in arr:
    print(j)