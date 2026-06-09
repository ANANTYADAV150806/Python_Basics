text = input("enter the list:")
list = text.split(",")
print("the enters list is :" , list)
k = int(input("from which positiion do you wanna slice the list:"))
new_list = list[0:k]
print("the sliced list is:", new_list)