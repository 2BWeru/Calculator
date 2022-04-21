# calculator

# lets create instances which the user will be able to choose calculator function
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

# lets create a variable for  input command

choice = input("Enter your choice :")

# lets create variables for the two inputs

num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))

# calculator the logic
 
#  if user inputs "1" then we add
if choice == "1":
    print(num1, "+", num2, "=", (num1+num2))

# elif user inputs num "2" we subtract
elif choice == "2":
    print(num1,"-",num2,"=",(num1-num2))

# elif user inputs num "3" we multiply
elif choice == "3":
    print(num1,"*",num2,"=",(num1*num2))
    
# elif user inputs num 4 we divide 
elif choice == "4":
    if num2 == 0.0:
        print( "Divide by 0 error")
    else:
        print(num1,"/",num2,"=", (num1/num2))

# if user selects num above 4 
else:
    print("Invalid choice")