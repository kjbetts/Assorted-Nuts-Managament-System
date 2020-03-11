#Kearney Betts
#CIS 125-70
# Assignment 5

# Input
nuts = []
textfile = open("nutsDB.txt", "r")

# Process
for x in textfile:
    nuts.append(x.split(","))


# Output
print("Welcome to the Nutty Nut Catalog ")
print("*******************************")
print("Please Make yout Selection\n")
choice = input("1. Display Nuts Catalog \n2. Display Almonds Selections \n3. DIsplay Cocunut Selection \n4. Item Number 12110 - 12160 \n5. Don't Display Nuts that are Raw \n\nEnter your Selection:  ")

# Displays the Nuts Catalog
if choice ==  "1":
    f = open("nutsDB.txt", "r")
    for x in f:
          print(x)

# Almonds Selections
if choice ==  "2":
    f = open("nutsDB.txt", "r")
    for x, line in enumerate(f):
        if x == 4:
            print(line)
        if x == 5:
             print(line)
        if x == 6:
            print(line)
        if x == 7:
            print(line)
        if x == 8:
            print(line)

# Coconuts Selections
if choice == "3":
     f = open("nutsDB.txt", "r")
     for x, line in enumerate(f):
        if x == 27:
            print(line)
        if x == 28:
            print(line)
        if x == 29:
            print(line)
        if x == 30:
            print(line)
        if x == 31:
            print(line)
        if x == 32:
            print(line)
        if x == 33:
            print(line)
        if x == 34:
            print(line)

# Item Number 12110 - 12160
if choice == "4":
     f = open("nutsDB.txt", "r")
     for x, line in enumerate(f):
        if x == 28:
            print(line)
        if x == 29:
            print(line)
        if x == 30:
            print(line)
        if x == 31:
            print(line)
        if x == 32:
            print(line)
        if x == 33:
            print(line)
        if x == 34:
            print(line)
        if x == 35:
            print(line)
        if x == 36:
            print(line)
        if x == 37:
            print(line)
        if x == 38:
            print(line)
        if x == 39:
            print(line)
        if x == 40:
            print(line)
        if x == 41:
            print(line)
        if x == 42:
            print(line)
        if x == 43:
            print(line)
        if x == 44:
            print(line)
        if x == 45:
            print(line)
        if x == 46:
            print(line)
        if x == 47:
            print(line)
        if x == 48:
            print(line)
        if x == 49:
            print(line)
        if x == 50:
            print(line)
        if x == 51:
            print(line)
        if x == 52:
            print(line)
        if x == 53:
            print(line)
        if x == 54:
            print(line)
        if x == 55:
            print(line)
        if x == 56:
            print(line)
        if x == 57:
            print(line)
        if x == 58:
            print(line)
        if x == 59:
            print(line)
        if x == 60:
            print(line)
        if x == 61:
            print(line)

#Dont Display Nuts that are Raw
if choice == "5":
      f = open("nutsDB.txt", "r")
      for x, line in enumerate(f):
         if x == 2:
            print(line)
         if x == 3:
            print(line)
         if x ==4:
            print(line)
         if x == 5:
            print(line)
         if x == 6:
            print(line)
         if x == 7:
            print(line)
         if x == 8:
            print(line)
         if x == 9:
            print(line)
         if x == 10:
            print(line)
         if x == 11:
            print(line)
         if x == 12:
            print(line)
         if x == 13:
            print(line)
         if x == 15:
            print(line)
         if x == 17:
            print(line)
         if x == 18:
             print(line)
         if x == 19:
             print(line)
         if x == 23:
             print(line)
         if x == 24:
             print(line)
         if x == 26:
            print(line)
         if x == 27:
            print(line)
         if x == 28:
            print(line)
         if x == 29:
            print(line)
         if x == 31:
             print(line)
         if x == 33:
            print(line)
         if x == 34:
             print(line)
         if x == 35:
             print(line)
         if x == 36:
             print(line)
         if x == 37:
             print(line)
         if x == 39:
             print(line)
         if x == 40:
             print(line)   
         if x == 41:
             print(line)
         if x == 43:
             print(line)
         if x == 44:
             print(line)
         if x == 45:
             print(line)
         if x == 46:
             print(line)
         if x == 47:
             print(line)
         if x == 48: 
            print(line)
         if x == 49:
            print(line)
         if x == 50:
             print(line)
         if x == 51:
             print(line)
         if x == 52:
             print(line)
         if x == 53:
             print(line)
         if x == 54:
             print(line)
         if x == 55:
            print(line)            
         if x == 57:
            print(line)
         if x == 58:
            print(line)
         if x == 59:
            print(line)
         if x == 60:
            print(line)
         if x == 61:
            print(line)


      
