def bmi_status(value):
    if value < 18.5:
        print("you are underweight")
    if (18.5 < value) and (value < 24.9):
        print("yu are normal weight")
    if 25.0 < value and value < 29.9:
        print("yu are oveweight")
    if 30.0 < value:
        print("yu are obese")

def metric_system(kg, meter):
    return (kg / (meter**2))

def imperial_system(pound, inch):
    return pound * 703 / (inch**2)

status = True

while status:
    print("-----------------------------------")
    print("1.Metric system (kg,meter)")
    print("2.Imperial system (pound,inch)")
    print("-----------------------------------")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("===============================")
        kg = float(input("Enter the weight (kg): "))
        meter = float(input("Enter the height (meter): "))
        print("===============================")

        bmi = metric_system(kg, meter)
        print("your bmi: ", bmi)
        bmi_status(bmi)

    elif choice == 2:
        print("===============================")
        pound = float(input("Enter the weight (lbs): "))
        inch = float(input("Enter the height (inch): "))
        print("===============================")

        bmi = imperial_system(pound, inch)
        print("your bmi: ", bmi)
        bmi_status(bmi)
    else:
        exit()