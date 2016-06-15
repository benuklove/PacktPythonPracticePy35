"""
Created on 6/15/2016 by Ben

Sum of even valued Fibonacci terms whose values do not exceed N,
given T test cases
"""


# Number of test cases, T
T = int(input().strip())

i = 0
arr = []
while i < T:
    # Whose values do not exceed, N
    N = int(input().strip())
    total, a, b = 0, 1, 2
    while b <= N:
        # Sum the even fib numbers
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    i += 1
    # Put those sums into the list for stdout
    arr.append(total)

# Output each sum of even fib numbers on a new line
for j in arr:
    print(j)
