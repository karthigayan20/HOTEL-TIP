########## TIP GENERATOR CODE ##########

print("Welcome to the tip generator")

bill=float(input("what was the total bill? $ "))
tip =int(input("How much tip would you like to give ? 5,10,15,20? "))
people = int(input("How many people to spilt the bill? "))

tip_percent=tip/100
total_tip_bill=bill*tip_percent
total_bill=bill + total_tip_bill

split_person=round(total_bill / people , 2)

print(f"Each person should pay: ${split_person}")



