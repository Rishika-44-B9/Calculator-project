print("Simple Calculator")
num1 = float(input("Enter first number:"))
num1 = float(input("Enter first number:"))

print("1.Add  2.Subtract  3.Multiply  4,Divide")
choice = input("Choose operation:")
if choice=="1":
    print("Result:", num1+num2)
elif choice=="2":
    print("Result:", num1-num2)
elif choice=="3":
    print("Result:", num1*num2)
elif choice=="4":
    if num2 != 0:
        print("Result",num1 / num2)
        else:
            print("Cannot divide by zero")
            else:
                print("Invalid choice")
   