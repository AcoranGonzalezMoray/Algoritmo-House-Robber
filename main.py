from solve_memoization import *
from solve_tabulation  import *

first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

value1        = solve_memoization(items)
value2, taken = solve_tabulation(items)

assert value1 == value2

print(value1)
print(taken)