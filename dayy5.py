# Nested For Loop Practice Problems
# 1. Seating Arrangement Checker
# Task: Find occupied seats, empty seats, and row with maximum occupancy.
# Input: seats=[[1,0,1,1],[0,1,1,0],[1,1,1,1]]
# Output: Occupied Seats=9, Empty Seats=3, Row with Maximum Occupancy=Row 3

seats=[[1,0,1,1],[0,1,1,0],[1,1,1,1]]
occ = 0
empty = 0
rowmaxocc = 0
row = 0
for i in range(len(seats)):
    count = 0
    for j in range(len(seats[i])):
        if seats[i][j] == 1:
            occ += 1
            count += 1
        else:
            empty += 1
    if count > rowmaxocc:
        rowmaxocc = count
        row = i + 1
print("Occupied Seats =", occ)
print("Empty Seats =", empty)
print("Row with Maximum Occupancy = Row", row)







# 2. Product Price Comparison
# Task: Find cheapest price for each product and store.
# Input: prices=[[100,120,90],[250,200,300],[50,70,60]]
# Output: Product 1=90(Store 3), Product 2=200(Store 2), Product 3=50(Store 1)

prices = [[100,120,90],[250,200,300],[50,70,60]]
for i in range(len(prices)):
    minprice = prices[i][0]
    store = 1
    for j in range(len(prices[i])):
        if prices[i][j] < minprice:
            minprice = prices[i][j]
            store = j + 1
    print("Product", i+1, "=", minprice, "(Store", store, ")")


# 3. Word Search in a Grid
# Task: Count occurrences of a given character.
# Input: grid=[['p','y','t'],['h','o','n'],['p','y','t']], character='p'
# Output: p found 2 times

grid = [['p','y','t'],['h','o','n'],['p','y','t']]
ch = 'p'
count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ch:
            count += 1
print(ch, "found", count, "times")


# 4. Matrix Diagonal Analyzer
# Task: Find diagonal sums and compare them.
# Input: matrix=[[5,2,3],[1,6,4],[7,8,9]]
# Output: Main=20, Opposite=16, Equal=False

matrix = [[5,2,3],[1,6,4],[7,8,9]]
main = 0
opp = 0
for i in range(len(matrix)):
    main += matrix[i][i]
    opp += matrix[i][len(matrix)-1-i]
print("Main =", main)
print("Opposite =", opp)
print("Equal =", main == opp)


# 5. Password Strength Analyzer
# Task: Count uppercase, lowercase and digits and classify password.
# Input: passwords=['Abc123','hello','P@55']
# Output: Abc123 Strong, hello Weak, P@55 Strong

passwords = ['Abc123','hello','P@55']
for p in passwords:
    upper = 0
    lower = 0
    digit = 0
    for ch in p:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
    if upper > 0 and lower > 0 and digit > 0:
        print(p, "Strong")
    else:
        print(p, "Weak")






# 6. Image Pixel Brightness Analyzer
# Task: Count dark, medium and bright pixels.
# Input: image=[[20,80,200],[40,150,220]]
# Output: Dark=2, Medium=2, Bright=2

image = [[20,80,200],[40,150,220]]
dark = 0
medium = 0
bright = 0
for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j] < 50:
            dark += 1
        elif image[i][j] <= 150:
            medium += 1
        else:
            bright += 1
print("Dark =", dark)
print("Medium =", medium)
print("Bright =", bright)


# 7. Find Duplicate Rows in Data
# Task: Find rows containing identical data.
# Input: data=[[10,20,30],[40,50,60],[10,20,30]]
# Output: Duplicate Row Found: Row 1 and Row 3

data = [[10,20,30],[40,50,60],[10,20,30]]
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] == data[j]:
            print("Duplicate Row Found: Row", i+1, "and Row", j+1)




# 8. Bus Route Analyzer
# Task: Find common stops and total unique stops.
# Input: routes=[['A','B','C'],['B','C','D'],['C','D','E']]
# Output: Common Stop=C, Total Unique Stops=5

routes = [['A','B','C'],['B','C','D'],['C','D','E']]
common = []
for stop in routes[0]:
    if stop in routes[1] and stop in routes[2]:
        common.append(stop)
unique = []
for row in routes:
    for stop in row:
        if stop not in unique:
            unique.append(stop)
print("Common Stop =", common[0])
print("Total Unique Stops =", len(unique))



# 9. Monthly Expense Category Tracker
# Task: Find highest expense and categories above limit.
# Input: expenses=[[500,200,800],[300,700,100],[900,400,600]], limit=500
# Output: Person 1 Highest=800, Categories Above Limit=4

expenses = [[500,200,800],[300,700,100],[900,400,600]]
limit = 500
count = 0
for i in range(len(expenses)):
    high = expenses[i][0]
    for j in range(len(expenses[i])):
        if expenses[i][j] > high:
            high = expenses[i][j]
        if expenses[i][j] > limit:
            count += 1
    print("Person", i+1, "Highest =", high)
print("Categories Above Limit =", count)



# 10. Chess Board Analyzer
# Task: Count white pieces, black pieces and empty positions.
# Input: board=[['W','B','-'],['B','W','-'],['-','W','B']]
# Output: White=3, Black=3, Empty=3

board = [['W','B','-'],['B','W','-'],['-','W','B']]
white = 0
black = 0
empty = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'W':
            white += 1
        elif board[i][j] == 'B':
            black += 1
        else:
            empty += 1
print("White =", white)
print("Black =", black)
print("Empty =", empty)