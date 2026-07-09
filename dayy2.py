# 1.Count Total Vowels
# Task: Write a function that takes a string and returns the total number 
# of vowels (a, e, i, o, u).
# Example Input: programming
# Example Output: Total Vowels = 3

def totNum(vowels):
    count=0
    for ch in vowels:
        if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
            count=count+1
    return count
print(f"total vowels={totNum('programming')}")






# 2.	Count Total Consonants
# Task: Write a function that takes a string and returns the total number of consonants.
# Example Input:
# python
# Example Output: Total Consonants = 5

def totNumCon(word):
    count=0
    for ch in word:
        if ch!="a" and ch!="e" and ch !="i" and ch!="o" and ch!="u":
            count=count+1
    return count
print(f"total consonents={totNumCon('python')}")




# 3.	Reverse a String
# Task: Write a function that takes a string and returns the string in reverse order.
# Example Input:
# computer
# Example Output:
# Reversed String = retupmoc

def revorder(word):
    rev=" "
    for ch in word:
          rev=ch+rev
    return rev

print(f"Reversed String ={revorder('computer')}")




# 4.	Count Uppercase and Lowercase Letters
# Task: Write a function that takes a string and returns the number of uppercase
#  and lowercase letters.
# Example Input: PyThOn
# Example Output:
# Uppercase = 3
# Lowercase = 3

def numOfUL(word):
    upper=0
    lower=0
    for ch in word:
        if "a"<=ch<="z":
            upper=upper+1
        elif "A"<=ch<= "Z":
            lower=lower+1  
    return upper, lower 
upper, lower = numOfUL("PyThOn")    
print("uppercase=",upper )
print("lowercase=",lower)







# 5.	Count Digits in a String
# Task: Write a function that takes a string and returns how many digits are present.
# Example Input: abc12345xy
# Example Output:
# Digits = 5

def numDigits(word):
    count=0
    for ch in word:
        if "0"<=ch<="9":
            count=count+1
    return count
print("Digits =", numDigits("abc12345xy"))




# 6.	Check Palindrome
# Task: Write a function that takes a string and checks whether it is a palindrome.
# Example Input: madam
# Example Output: Palindrome

def palindrome(word):
    rev = ""
    for ch in word:
        rev = ch + rev
    if word == rev:
        return "Palindrome"
print(palindrome("madam"))





# 7.	Count Occurrences of a Character
# Task: Write a function that takes a string and a character and returns 
# how many times that character appears.
# Example Input:
# banana 
# a
# Example Output: Occurrences = 3

def charApp(word,letter):
    count=0
    for ch in word:
        if ch==letter:
            count=count+1
    return count
print(f" Occurrences={charApp("banana","a")}")
   




# 8.	Find the Longest Word
# Task: Write a function that takes a sentence and returns the longest word.
# Example Input:
# Python is an amazing language
# Example Output: Longest Word = language

def longWord(word):
    largest=""
    for ch in word.split():
        if len(ch)>len(largest):
            largest=ch
    return largest
print(f" Longest Word = {longWord('Python is an amazing language')}")




# 9.	Remove All Spaces
# Task: Write a function that takes a sentence and returns the same sentence after
#  removing all spaces.
# Example Input: Data Science is fun
# Example Output: DataScienceisfun

def remSpaces(word):
    removingspace="" 
    for ch in word:
        if ch!= " ":
            removingspace = removingspace + ch

    return removingspace

print(remSpaces("Data Science is fun"))





# 10.	Count Words in a Sentence
# Task: Write a function that takes a sentence and returns the total number of words.
# Example Input:
# Learning Python is very interesting
# Example Output:
# Total Words = 5

def totNumWords(word):
    count=0
    for ch in word.split():
        count=count+1
    return count

print(f"Total Words = {totNumWords('Learning Python is very interesting')}")    
    


