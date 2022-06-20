# Author -> Luis Oliveros
# Version -> 6/20/2022
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def subtract(x, y):
    return x - y

def expontent(x, y):
    return x ** y

def modulo(x, y):
    return x % y



print("Exit calculator at anytime with [exit]\n")
carry = 0

while True:
    user_input = input("\nChoose Operation.\nAddition         [1]\nSubtraction " + 
                        "     [2]\nMultiplication   [3]\nDivision " +
                        "        [4]\nExponential      [5]\nModulus" +
                        "          [6]\nClear Calculator [7]\n")

    if user_input in ('1', '2', '3', '4','exit','5','6','7'):

        if user_input == '7':
            carry = 0
            continue
        
        if user_input == 'exit':
            break

        if carry != 0:
            temp = 0 
            temp = carry
            num1 = float(input("\nenter number: "))

            if user_input == '1':
                carry = add(carry, num1) 
                print(str(temp) + " + " + str(num1) + " = " + str(carry))

            elif user_input == '2':
                carry = subtract(carry, num1) 
                print(str(temp) + " - " + str(num1) + " = " + str(carry))

            elif user_input == '3':
                carry = multiply(carry, num1) 
                print(str(temp) + " * " + str(num1) + " = " + str(carry))

            elif user_input == '4':
                carry = divide(carry, num1) 
                print(str(temp) + " / " + str(num1) + " = " + str(carry))
            
            elif user_input == '5':
                carry = expontent(carry, num1) 
                print(str(temp) + " ^ " + str(num1) + " = " + str(carry))
            
            elif user_input == '6':
                carry = modulo(carry, num1) 
                print(str(temp) + " % " + str(num1) + " = " + str(carry))

        else:
            num1 = float(input("\nenter first number: "))
            num2 = float(input("enter second number: "))

            if user_input == '1':
                carry = add(num1, num2) 
                print(str(num1) + " + " + str(num2) + " = " + str(carry))

            elif user_input == '2':
                carry = subtract(num1, num2) 
                print(str(num1) + " - " + str(num2) + " = " + str(carry))

            elif user_input == '3':
                carry = multiply(num1, num2) 
                print(str(num1) + " * " + str(num2) + " = " + str(carry))

            elif user_input == '4':
                carry = divide(num1, num2) 
                print(str(num1) + " / " + str(num2) + " = " + str(carry))

            elif user_input == '5':
                carry = expontent(num1, num2) 
                print(str(num1) + " ^ " + str(num2) + " = " + str(carry))
            
            elif user_input == '6':
                carry = modulo(num1, num2) 
                print(str(num1) + " % " + str(num2) + " = " + str(carry))

    else:
        print("Invalid Input")


 