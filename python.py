print("hello world!")
name = "anant"
print ("my name is " + name)
a = 20
b = 40
d = 200
sum = a+b
difference = b-a
c = (sum * difference) - d
print("the value of c is " + str(c))
if c > 1000:
    print("c is greater than 1000")
elif c < 1000:
    print ("c is less than 1000")
else: print ("c is equal to 1000")



a = input("pls enter value:")
print ("the value you entered is " + a)
b = input("pls enter the value 2 :")
print ("the value you entered is " + b)
c = int(a) * int(b)
if c > 1000:
    print("the value of multiplication is greater than 1000")
elif c < 1000:
    print("the value of multiplication is less than 1000")
else:
    print("the value of multiplication is equal to 1000")

fruits= ["apple", "banana", "dragonfruit","kiwi"]
print(fruits[2])
fruits.append("orange")
print(fruits)
for fruit in fruits:
    print(fruit + "is a very healthy fruit")
    
count = 1
while count <= 20:
    print(count)
    count = count + 1
