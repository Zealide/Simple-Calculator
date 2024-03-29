calculation = input ("What basic operator do you want to use? (+, -, *, /)\n")
first_Number = int(input ("What is the first number?\n"))
second_Number = int(input ("What is the second number?\n"))

if calculation == "+":
    print (f"{first_Number} + {second_Number} =", first_Number + second_Number)

elif calculation == "-":
    print (f"{first_Number} - {second_Number} =", first_Number - second_Number)

elif calculation == "*":
    print (f"{first_Number} * {second_Number} =", first_Number * second_Number)

elif calculation == "/":

    if second_Number == 0:
        print("You cant divide with Zero")
    else:
        print (f"{first_Number} / {second_Number} =", first_Number / second_Number)
