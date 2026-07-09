# 10 Basic Arithmetic Operation Real-Time Python Problems (Functions)
# 1.	Grocery Bill
# Write a function that takes the prices of 5 items and returns the total bill.
# Example Input:
# 10
# 25
# 15
# 30
# 20
# Output:
# Total Bill = 100

def bill(item1,item2,item3,item4,item5):
    totalbill=item1+item2+item3+item4+item5
    return totalbill
price1=int(input("enter price of item1:"))
price2=int(input("enter price of item2:"))
price3=int(input("enter price of item3:"))
price4=int(input("enter price of item4:"))
price5=int(input("enter price of item5:"))

total = bill(price1, price2, price3, price4, price5)
print("totalbill =", total)




# 2.	Student Percentage
# Write a function that takes marks in 5 subjects and returns the percentage.
# Example Input:
# 80
# 75
# 90
# 85
# 70
# Output:
# Percentage = 80.0

def  marks(sub1,sub2,sub3,sub4,sub5):
    percentage=(sub1+sub2+sub3+sub4+sub5)/5
    return percentage
sub1=int(input("enter sub1:"))
sub2=int(input("enter sub2:"))
sub3=int(input("enter sub3:"))
sub4=int(input("enter sub4:"))
sub5=int(input("enter sub5:"))

totPercentage=marks(sub1,sub2,sub3,sub4,sub5)
print("percentage= ", totPercentage )



# 3.	Restaurant Bill Split
# Write a function that takes the total restaurant bill and the number of friends and 
#  how much each person should pay.
# Example Input:
# 1200
# 4
# Output:
# Each Person Pays = 300.0

def totBill(totalbill,friends):
    each_person=totalbill/friends
    print("each person pays=",each_person )
totalBill=int(input("enter totalbill:"))
friends=int(input("enter number of friends:"))

totBill(totalBill,friends)





# 4.	Monthly Salary
# Write a function that takes daily wage and number of working days and returns the monthly salary.
# Example Input:
# 800
# 26
# Output:
# Monthly Salary = 20800

def MonthSal(dailywage,numberOfWorkingDays):
    MonthSalary=dailywage*numberOfWorkingDays
    print("Monthly Salary=",MonthSalary)
    return MonthSal
dailywage=int(input("enter dailywage:"))
numberOFWorkingDays=int(input("enter numberOFWorkingDays:"))

MonthSal(dailywage,numberOFWorkingDays)




# 5.	Cricket Strike Rate
# Write a function that takes runs scored and balls faced and returns the strike rate.
# Formula: (runs × 100) / balls
# Example Input:
# 72
# 48
# Output:
# Strike Rate = 150.0

def strikeratee(runs,balls):
    strikerate=(runs*100) / balls
    print("strikerate=",strikerate)
runs=int(input("enter scored runs:"))
balls=int(input("enter bills:"))

strikeratee(runs,balls)





# 6.Area and Perimeter of a Rectangle
# Write a function that takes length and breadth and returns both area and perimeter.
# Example Input:
# 12
# 8
# Output:
# Area = 96
# Perimeter = 40
# Area = Length × Breadth
# Perimeter = 2 × (Length + Breadth)

def bothAP(Length,Breadth):
    Area = Length *Breadth
    Perimeter = 2 *(Length + Breadth)
    print("Area:",Area)
    print("Perimeter:",Perimeter)
    return Area,Perimeter
Length=int(input("enter Length:"))
Breadth=int(input("enter Breadth:"))
bothAP(Length,Breadth)





# 7.	Electricity Bill
# Write a function that takes units consumed and price per unit and returns the total bill.
# Example Input:
# 150
# 8
# Output:
# Electricity Bill = 1200

def totbill(price,units):
    totalbill=price*units
    print("totalbill:",totalbill)
    return totalbill
price=int(input("enter price:"))
units=int(input("enter units:"))
totbill(price,units)





# 8.	Simple Interest
# Write a function that takes principal, rate, and time and returns the simple interest.
#  Formula: (P × R × T) / 100
# Example Input:
# 50000
# 8
# 2
# Output:
# Simple Interest = 8000.0

def simpleInterest(P,R,T):
    simpInterest=(P * R *T) / 100
    print("simpInterest:",simpInterest)
    return simpleInterest
P=int(input("enter P:"))
R=int(input("enter R:"))
T=int(input("enter T:"))
simpleInterest(P,R,T)





# 9.	Bike Mileage
# Write a function that takes distance traveled and fuel used and returns the mileage. 
# Formula: Distance / Fuel
# Example Input:
# 240
# 6
# Output:
# Mileage = 40.0 km/l

def milage(Distance,Fuel):
    mil=Distance / Fuel
    print("mil:",mil)
    return milage
Distance=int(input("enter Distance:"))
Fuel=int(input("enter Fuel:"))
milage(Distance,Fuel)




# 10.	Exam Remaining Marks
# Write a function that takes total marks and obtained marks and returns the remaining marks.
# Example Input:
# 600
# 482
# Output:
# Remaining Marks = 118


def remainingMarks(totmarks,obtmarks):
    remMarks=totmarks-obtmarks
    print("remMarks:",remMarks)
    return remainingMarks
totmarks=int(input("totmarks:"))
obtmarks=int(input("enter obtmarks"))
remainingMarks(totmarks,obtmarks)