import itertools
import math

cities = ["A", "B","C", "D", "E"]
start = cities[0]
end = cities[-1]

remaining_cities = cities[1:-1]

# print(remaining_cities)

perms = itertools.permutations(remaining_cities)

# for p in perms:
#     print(p)
# permutations = [[start] + list(p) + [end] for p in perms]
# print(permutations)
