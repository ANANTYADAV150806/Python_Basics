nums = input("enter the numbers you want to sort:")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [int(x) for x in nums.split() if x.strip()]
print("Sorted numbers:", bubble_sort(numbers))
even_numbers = [ num for num in numbers if num % 2 == 0]
odd_numbers = [ num for num in numbers if num % 2 != 0 ]
print("sorted even number : ", even_numbers )
print ( "sorted odd numbers :" , odd_numbers)
