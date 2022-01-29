

#Calculates the area of a trapezoid

print ("This program calculates the area of a trapezoid.")

#Get height of the trapezoid from user
height = float(input("Enter the height of the trapezoid:"))

#Get length of the bottom base from user
bottom_base = float(input("Enter the length of the bottom base:"))

#Get length of the top base from user
top_base = float(input("Enter the length of the top base:"))

#Calculate and print the answer
area = float(1/2 *(bottom_base + top_base) * (height))
print("The area is:", (round (area, 2)))



