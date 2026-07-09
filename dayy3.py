# Beginner List Practice Set
# 1. Count Even Numbers
# Write a function that returns the number of even numbers in a list.
# Example
# Input: [2, 5, 8, 11, 14]
#  Output: 3

def evenNums(num):
    count=0
    for i in num:
       if i %2 ==0:
           count=count+1
    return count
print(evenNums([2, 5, 8, 11, 14]))







# 2. Find the Largest Element
# Return the largest element in a list.
# Example
# Input: [12, 45, 7, 89, 23] 
# Output: 89

def largestNum(num):
    largest=num[0]
    for i in num:
        if i>largest:
            largest=i
    return largest
print(largestNum([12, 45, 7, 89, 23]))








# 3. Find the Smallest Element
# Return the smallest element in a list.
# Example
# Input: [12, 45, 7, 89, 23] Output: 7

def smallestNum(num):
    smallest=num[0]
    for i in num:
        if i<smallest:
            smallest=i
    return smallest
print(smallestNum([12, 45, 7, 89, 23]))






# 4. Reverse a List
# Return the list in reverse order.
# Example
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def returnList(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev = rev + [lst[i]]
    return rev
print(returnList([1, 2, 3, 4, 5]))







# 5. Sum of All Elements
# Return the sum of all numbers in the list.
# Example
# Input: [4, 8, 10] Output: 22

def sumAllEle(num):
    sum=0
    for i in num:
          sum=sum+i
    return sum
print(sumAllEle([4, 8, 10] ))






# 6. Count Occurrences
# Count how many times a target appears.
# Example
# Input: List=[1,2,3,2,4,2], Target=2 Output: 3

def tarAppears(list,num):
    count=0
    for i in list:
        if i==num:
            count=count+1
    return count       
print(tarAppears([1,2,3,2,4,2],2))





# 7. Remove Duplicates
# Remove duplicates while preserving order.
# Example
# Input: [1,2,2,3,1,4] Output: [1,2,3,4]

def remDupli(lst):
    new = []
    for i in lst:
        if i not in new:
            new = new + [i]
    return new
print(remDupli([1, 2, 2, 3, 1, 4]))







# 8. Find the Average
# Return the average of all numbers.
# Example
# Input: [10,20,30,40] Output: 25.0


def average(list):
    total = 0
    for i in list:
        total = total + i
    avg = total / len(list)
    return avg
print(average([10, 20, 30, 40]))







# 9. Create a List of Squares
# Return a new list containing the square of every element.
# Example
# Input: [2,3,4,5]
# Output: [4,9,16,25]

def square(list):
    squares=[]
    for i in list:
        squares = squares + [i ** 2]
    return squares
print(square([2,3,4,5]))





# 10. Count Positive Numbers Return the number of positive numbers.
# Example
# Input: [-2,5,0,7,-1,9]
# Output: 3

def posNum(num):
    count=0
    for i in num:
        if i >0:
            count=count+1
    return count
print(posNum([-2,5,0,7,-1,9]))


