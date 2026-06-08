List = list(input("enter the list of elements you want to rotate:"))
k = int(input("enter the number of positions you want to rotate the list:"))
k = k % len(List)
reversed_list = List[k:] + List[:k]
print("the rotated list is:" , reversed_list)