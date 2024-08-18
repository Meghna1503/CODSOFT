
print("CALCULATOR\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division"
      "5.Power")
operation_choice = int(input("enter your choice: "))
if operation_choice in range(1, 5):
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))

    if operation_choice == 1:
        num3 = num1 + num2
        print("the sum of two number is : ", num3)
    elif operation_choice == 2:
        num4 = num1 - num2
        print("the subtraction of two number is : ", num4)
    elif operation_choice == 3:
        num5 = num1*num2
        print("the multiplication of two number is : ", num5)
    elif operation_choice == 4:
        num6 = num1 / num2
        print("the Division of two number is : ", num6)
if operation_choice == 5:
    num7 = float(input("enter the number:"))
    num8 = int(input("enter power:"))
    num9 = num7**num8
    print("the power of two number is {:0.2f} ".format(num9))
else:
    print("invalid input")




