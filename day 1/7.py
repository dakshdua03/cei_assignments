# Q7 Create a program that prints the multiplication table of a given number using a while loop.
number = int(input("Enter a number to display its multiplication table: "))
counter = 1

while counter <= 10:
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1
