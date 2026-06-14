set_a = list(input("enter the list A:"))
set_b = list(input("enter the list B:"))
common_elements = [item for item in set_a if item in set_b]
print("common elements",common_elements)