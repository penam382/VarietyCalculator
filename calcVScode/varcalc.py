print("Hello, Welcome to my Variety Calculator!")
print("Choose between a: ")
print("1. Normal calculator (Type 1)")
print("2. BMI calulator (Type 2)")
print("3. Triangle calulator (Type 3)")
print("4. Tip calcultor(Type 4) ")

choice = input("Choose 1/2/3/4: " )

if choice == "1":
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

if choice == "2":
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    bmi = round(weight / height ** 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")

if choice == "3":
    import math
    math.sqrt(4)
    print("Welcome to the Triangle Calculator!")
    print("Fill in your answers and type a '0' for the number you don't.")

    sideA = (int(input("Side A: ")))

    sideB = (int(input("Side B: ")))

    sideC = (int(input("Hypotenuse: ")))

    if sideA is 0:
        sideA = math.sqrt((sideC**2) - (sideB**2))
        print("Side A =", sideA)

    if sideB is 0:
        sideB = math.sqrt((sideC**2) - (sideA**2))
        print("Side B =", sideB)
        
    if sideC is 0:
        sideC = math.sqrt((sideA**2) + (sideB)**2)
        print("Side C =", sideC)

if choice == "4":
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
    people_amount = int(input("How many people split the bill? "))

    total_tip = (tip*.01+1)

    bill = (total_bill / people_amount * total_tip)

    print(f"Each person should pay: ${bill:.2f}.") 
