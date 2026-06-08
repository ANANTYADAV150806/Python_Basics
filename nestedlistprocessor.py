import ast

user_input = input("Enter the list you want to process: ").strip()
if "=" in user_input:
    user_input = user_input.split("=", 1)[1].strip()

nested_list = ast.literal_eval(user_input)

flat_list = [item for sublist in nested_list for item in sublist]
even_numbers = [num for num in flat_list if num % 2 == 0]
sum_of_squares = [num * num for num in even_numbers]

print("The flat list is:", flat_list)
print("The even numbers in the list are:", even_numbers)
print("The sum of squares of the even numbers in the list are:", sum_of_squares)

