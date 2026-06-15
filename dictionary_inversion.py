d = {}
n = int(input("Enter number of key-value pairs: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print("Original dictionary:", d)
inverted = {}
for key, value in d.items():
    inverted.setdefault(value, []).append(key)
print("Inverted dictionary:", inverted)