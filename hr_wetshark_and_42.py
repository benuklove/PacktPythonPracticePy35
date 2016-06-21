"""

  Created on 6/20/2016 by Ben

  Hacker Rank's problem: All Domains/Mathematics/Algebra/Wet Shark and 42

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
arrb = []
while i < T:
    #  Original Strength, S
    S = int(input().strip())
    if S < 1 or S > 10**18:
        continue
    multiple = S // 21
    square = (S * 2) + (2 * multiple)
    if S > 420:
        # new_mult = S // 420
        # square += 2 * new_mult
        new_mult = S // 210
        square += new_mult
#  NEW/OLD SECTION
    squareb = 1
    while S > 0:
        if squareb % 2 == 0 and squareb % 42 != 0:
            S -= 1
        squareb += 1
#  END OF NEW/OLD SECTION
    i += 1

    #  Put those sums into the list for stdout
    arr.append(square % (10**9 + 7))
    arrb.append((squareb-1) % (10**9 + 7))

# Output each sum of even fib numbers on a new line
for j in arr:
    print("j is: ", j)

for k in arrb:
    print("k is: ", k)

#  do stuff
    # for square in range(1, S):
    #     if square % 2 == 0 and square % 42 != 0:

    # square = 1
    # if S % 2 == 0:
    #     s = S / 2
    #     for x in range(1, S, 2)
    #     while S > 0:
    #         if square % 2 == 0 and square % 42 != 0:
    #             S -= 1
    #         square += 1
    #     i += 1