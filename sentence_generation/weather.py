import random
ppl_in_line_chain = {
    0 : [0, 1, 0, 1, 1],
    1 : [0, 1, 0, 2, 2],
    3 : [3, 3, 4, 5, 3],
    4 : [4, 4, 4, 6, 5],
    5 : [5, 4, 4, 4, 6],
    6 : [5, 5, 5, 7, 7],
    7 : [7, 7, 7, 6, 6]
}

num_ppl_in_line = [random.choice(list(ppl_in_line_chain.keys()))]

for i in range(10):
    num_ppl_in_line.append(random.choice(ppl_in_line_chain[num_ppl_in_line[i]]))

print(num_ppl_in_line)
