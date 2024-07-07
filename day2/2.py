# Create a program that takes user input to add multiple elements to an array, then prints the final array

array = []
num_elements = int(input("How many elements would you like to add? "))

for i in range(num_elements):
    element = int(input("Enter an element: "))
    array.append(element)

print("Final array:", array)
