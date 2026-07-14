# Basic Unique Number Problems in Python
# 1. Sum of First and Last Digit
# Task: Given a number, find the sum of its first digit and last digit.
# Example Input: Number = 58392
# Example Output: First digit = 5, Last digit = 2, Sum = 7

num = int(input("Enter number: "))
last = num % 10
first = num
while first >= 10:
    first = first // 10
print("First digit =", first)
print("Last digit =", last)
print("Sum =", first + last)



# 2. Count Digits Greater Than 5
# Task: Count digits in a number that are greater than 5.
# Example Input: Number = 836921
# Example Output: Digits greater than 5 = 3
 
num = int(input("Enter number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit > 5:
        count += 1
    num = num // 10
print("Digits greater than 5 =", count)





# 3. Product of Digits at Odd Positions
# Task: Find product of digits present at odd positions from right side.
# Example Input: Number = 58294
# Example Output: Product = 64


num = int(input("Enter number: "))
position = 1
product = 1
while num > 0:
    digit = num % 10
    if position % 2 != 0:
        product *= digit
    position += 1
    num = num // 10
print("Product =", product)





# 4. Largest Digit Difference
# Task: Find difference between largest and smallest digit.
# Example Input: Number = 58392
# Example Output: Largest = 9, Smallest = 2, Difference = 7

num = int(input("Enter number: "))
largest=0
smallest=0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    num = num // 10
print("Largest =", largest)
print("Smallest =", smallest)
print("Difference =", largest - smallest)




# 5. Count Even and Odd Digits
# Task: Count even and odd digits in a number.
# Example Input: Number = 58392
# Example Output: Even digits = 2, Odd digits = 3

num = int(input("Enter number: "))
count=0
evenDigit=0
oddDigit=0
while num>0:
    digit=num%10
    if digit %2==0:
        evenDigit+=1
    else:
        oddDigit+=1
    num = num // 10
print("Even digits =", evenDigit)
print("Odd digits =", oddDigit)





# 6. Reverse Number Without Changing Middle Digit
# Task: Reverse first and last digits while keeping middle digits unchanged.
# Example Input: Number = 12345
# Example Output: Result = 52341

n = input("Enter a number: ")
first = n[0]
last = n[-1]
middle = n[1:-1]
result = last + middle + first
print("Result =", result)



# 7. Digit Sum Until Single Digit
# Task: Add digits repeatedly until one digit remains.
# Example Input: Number = 9876
# Example Output: Final Result = 3

num = int(input("Enter number: "))
while num >= 10:
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    num = total
print("Final Result =", num)


# 8. Second Largest Digit
# Task: Find the second largest digit in a number.
# Example Input: Number = 58392
# Example Output: Largest = 9, Second largest = 8

num = int(input("Enter number: "))
largest = -1
second = -1
while num > 0:
    digit = num % 10
    if digit > largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit
    num = num // 10
print("Largest =", largest)
print("Second Largest =", second)


# 9. Replace Zero Digits
# Task: Replace all zero digits with 9.
# Example Input: Number = 102030
# Example Output: Result = 192939

num = int(input("Enter number: "))
result = 0
place = 1
while num > 0:
    digit = num % 10
    if digit == 0:
        digit = 9
    result = result + digit * place
    place = place * 10
    num = num // 10
print("Result =", result)



# 10. Digit Position Finder
# Task: Find position of a digit in a number from right side.
# Example Input: Number = 58392, Digit = 3
# Example Output: Position = 3

num = int(input("Enter number: "))
search = int(input("Enter digit to find: "))
position = 1
found = False
while num > 0:
    digit = num % 10
    if digit == search:
        print("Position =", position)
        found = True
        break
    position += 1
    num = num // 10
if found == False:
    print("Digit not found")