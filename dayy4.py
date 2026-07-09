# 1. Count Total Keys
# Task:
# Write a function that returns the total number of keys in a dictionary.

# Example Input:
# {"a":10,"b":20,"c":30}

# Example Output:
# 3


def totKeys(dict):
    count=0
    for i in dict:
        count+=1
    return count
print(totKeys({"a":10,"b":20,"c":30}))



# 2. Find the Key with the Largest Value
# Task:
# Return the key whose value is the largest.

# Example Input:
# {"Math":78,"Science":92,"English":85}

# Example Output:
# Science


def larKey(keys):
    largestVal=0
    largestkey=" "
    for key in keys:
        if keys[key]>largestVal:
            largestVal=keys[key]
            largestkey=key
    return largestkey
print(larKey({"math":78,"science":92,"english":85}))





# 3. Find the Key with the Smallest Value
# Task:
# Return the key whose value is the smallest.

# Example Input:
# {"Math":78,"Science":92,"English":65}

# Example Output:
# English

marks={"math":78,"science":92,"english":65}
print(min(marks))



# 4. Sum of All Values
# Task:
# Return the sum of all values in the dictionary.

# Example Input:
# {"Pen":20,"Book":150,"Bag":500}

# Example Output:
# 670

def sumValues(dict):
    total=0
    for key in dict:
        total+=dict[key]
    return total
print(sumValues({"pen":20,"book":150,"bag":500}))






# 5. Count Even Values
# Task:
# Return how many values in the dictionary are even.

# Example Input:
# {"a":10,"b":7,"c":16,"d":5}

# Example Output:
# 2

def countEvenVal(dict):
    count=0
    for val in dict:
        if dict[val] %2==0:
           count+=1
    return count
print(countEvenVal({"a":10,"b":7,"c":16,"d":5}))







# 6. Count Values Greater Than a Target
# Task:
# Given a target number, count how many dictionary values are greater than it.

# Example Input:
# Dictionary={"A":45,"B":80,"C":65,"D":90}
# Target=70

# Example Output:
# 2

def target(d):
    count = 0
    target = 70
    for key in d:
        if d[key] > target:
            count += 1
    return count
print(target({"A":45, "B":80, "C":65, "D":90}))    







# 7. Create a Dictionary of Squares
# Task:
# Given a list of numbers, create a dictionary where the number is the key and its square is the value.

# Example Input:
# [2,3,4,5]

# Example Output:
# {2:4,3:9,4:16,5:25}

def sqDict(list):
   dict={}
   for num in list:
       dict[num]=num*num
   return dict
print(sqDict([2,3,4,5]))





# 8. Count Positive Values
# Task:
# Return the number of positive values in the dictionary.

# Example Input:
# {"a":-5,"b":10,"c":0,"d":8}

# Example Output:
# 2

def posiVal(dict):
    count=0
    for possival in dict:
        if dict[possival]>0:
            count=count+1
    return count
print(posiVal({"a":-5,"b":10,"c":0,"d":8}))






# 9. Find the Average of All Values
# Task:
# Return the average of all values in the dictionary.
# Example Input:
# {"A":10,"B":20,"C":30}
# Example Output:
# 20.0

def avgVal(dict):
    sum=0
    count=0
    for value in dict.values():
     count+=1
     sum+=value
    return sum/count
print(avgVal({"A":10,"B":20,"C":30}))





# 10. Reverse Key and Value
# Task:
# Create a new dictionary where the values become keys and the keys become values.
# Example Input:
# {"A":1,"B":2,"C":3}
# Example Output:
# {1:"A",2:"B",3:"C"}

def revVal(dict):
   dict1={}
   for key,value in dict.items():
      dict1[value]=key
   return dict1
print(revVal({"A":1,"B":2,"C":3}))