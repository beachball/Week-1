#Imperical calculation function
def impericalcalc():
    height = input("What is you height in inches? ")
    height = float(height)
    weight = input("What is your weight in pounds? ")
    weight = float(weight)
    print("Calcuating...")
    BMI = weight/height**2*703
    if BMI > 25:
        print("You are obese!")
    if BMI > 20 and BMI < 25:
        print("You are normal!")
    if BMI < 20:
        print("You are underweight!")
    BMI = str(BMI)
    print("Your BMI is:" + BMI)
    print("")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    else:
        exit()

#Metrical calculation function
def metriccalc():
    height2 = input("What is you height in meters? ")
    height2 = float(height2)
    weight2 = input("What is your weight in kilograms? ")
    weight2 = float(weight2)
    print("Calcuating...")
    BMI = weight2/height2**2
    if BMI > 25:
        print("You are obese!")
    if BMI > 20 and BMI < 25:
        print("You are normal!")
    if BMI < 20:
        print("You are underweight!")
    BMI = str(BMI)
    print("Your BMI is:" + BMI)
    print("")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    else:
        exit()

#Program start function
def start():
    print("")
    print("BMI Calculator")

    #Unit selection
    unit = input("Imperical or Metric System? ")

    #Code for the imperical part of the equation
    if unit == "Imperical" or unit == "imperical":
        impericalcalc()

    #Code for the Metric part of the equation
    if unit == "Metric" or unit == "metric":
        metriccalc()

#Start of the program
print("")
print("BMI Calculator")

#Unit selection
unit = input("Imperical or Metric System? ")

#Code for the imperical part of the equation
if unit == "Imperical" or unit == "imperical":
    impericalcalc()

#Code for the Metric part of the equation
if unit == "Metric" or unit == "metric":
    metriccalc()
