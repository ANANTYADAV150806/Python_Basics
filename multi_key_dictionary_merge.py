from collections import Counter
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = dict( Counter(d1)+ Counter(d2))
print(merged)