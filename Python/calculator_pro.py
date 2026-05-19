import calculator
try:
    num1 = float(input("entr first number "))
    num2 = float(input("enter second number "))
    print("Additon ",calculator.add(num1,num2))
    print("Subtraction ",calculator.sub(num1,num2))
    print("Multiplication ",calculator.mul(num1,num2))
    print("Division ",calculator.div(num1,num2))
except ValueError:
    print("invalid number please enter a valid number ")
