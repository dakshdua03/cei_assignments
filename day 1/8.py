# Q8 . Write a Python program that iterates through numbers 1 to 10 and prints each number. Use the
# continue statement to skip numbers that are divisible by 3. 
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)
