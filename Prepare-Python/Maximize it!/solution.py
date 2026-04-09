from itertools import product

# Read K and M
k, m = map(int, input().split())

# Read each list, squaring elements and taking modulo immediately
# We use a set to remove duplicates, which can significantly reduce iterations (all done but only 1 done)
lists = []
for _ in range(k):
    # Skip the first element (the size Ni) and square the rest
    row = set(int(x)**2 % m for x in input().split()[1:])
    lists.append(row)
    
# Generate all possible combinations
max_s = 0
for combination in product(*lists):
    current_sum = sum(combination) % m
    if current_sum > max_s:
        max_s = current_sum
        
print(max_s)