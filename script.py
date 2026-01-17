print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill + bill * (tip/100)
bill_per_individual = bill_with_tip/people
print(f"The bill per individual is: ${round(bill_per_individual,2)}")
