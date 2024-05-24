#for adding the numbers
def add(x, y):
    return x + y

#for subtracting the numbers
def subtract(x, y):
    return x - y

#for multiplication of numbers
def multiply(x, y):
    return x * y

#for division of numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error:Division by Zero"

while True:
    #Get User Input
    num1 = float(input("Enter first number: "))
    operation=input("Enter operation(+,-,*,/):")
    num2 = float(input("Enter second number: "))

    # Perform calculation based on user's choice
    if operation=="+":
        result=add(num1, num2)
    elif operation=="-":
         result=subtract(num1, num2)
    elif operation=="*":
         result=multiply(num1, num2)
    elif operation=="/":
         result=divide(num1, num2)
    else:
        print("Invalid operation.please enter +,-,*,/.")
        continue
    
    #Display Result
    print(f"Result:{result}")

    #condition for next calculation
    another_calculation = input("Do you want to perform another calculation? (Yes/No): ").lower()
    if another_calculation !='yes':
        break