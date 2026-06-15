from itertools import permutations
s = input("Enter a string: ")
result = set(permutations(s))
print(f"\nAll permutations of '{s}':")
for i, p in enumerate(sorted(result), 1):
    print(f"{i}. {''.join(p)}")
print(f"\nTotal permutations: {len(result)}")