"""

  Created on Tues Jun 14 19:28:31 2016

  @author: Ben Love

  Find sum of multiples of 3 and 5 below n.

"""


def multsum(x):
    summ = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            summ += int(i)
    return summ

inputs = int(input().strip())
if inputs > 10 ** 5 or inputs < 1:
    print("Sorry, wrong number of inputs")
else:
    i = 0
    arr = []
    while i < inputs:
        x = int(input().strip())
        if x <= 10 ** 9 and x >= 1:
            arr.append(multsum(x))
            i += 1
        else:
            print("N is out of bounds")
            break
    for j in arr:
        print(j)
