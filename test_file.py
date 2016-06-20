import itertools

kitty_list = []
katty_list = []


for i in range(-7, 40):
    if i % 3 == 1:
        kitty_list.append(i)
    if i % 3 == 2:
        katty_list.append(i)

print(kitty_list)
print(katty_list)


blocks = list(range(1, 4))
print(blocks)
perms = list(itertools.permutations(blocks, 2))
print(perms)

print(type(perms[0][1]))
count = 0
for item in perms:
    for term in item:
        if term == 1:
            count += 1
print(count)


# def some_func(block_list):
#     temp_blocks = block_list.copy()
#     for item in temp_blocks:
#         a = item
#         temp_blocks.remove(item)
