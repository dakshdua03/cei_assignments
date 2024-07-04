# Create a program that stops printing numbers when it encounters a number greater than 5 using the
# break statement. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number > 5:
        break
    print(number)
