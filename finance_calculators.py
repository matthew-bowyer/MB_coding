#A tool to calculate simple or compound interest on a deposit
#or to calculate the monthly repayment on a house loan

import math

#Welcome message telling user what to do

print("""Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan.""")

user_entry=input("Enter either “investment” or “bond” to proceed: ")

#Data collection for investment calculation

if user_entry == "investment" or user_entry == "INVESTMENT" or user_entry == "Investment":
    amount=float(input("please enter the amount of money you are depositing "))
    interest=int(input("please enter the interest rate "))
    duration=int(input("please enter the number of years you investing  "))
    rate=input("please select simple or compound interest ")

#Simple interest calculation

    if rate == "simple":
        total_investment = round( amount * (1 + (interest/100) * duration), 2)
  
#Compound interest calculation

    elif rate == "compound":
        total_investment = round( amount * math.pow((1 + (interest/100)), duration), 2)

#Error message if wrong interest entered

    else:
        print("Invalid interest type. \
        Please enter simple or compound.")

#Output the total investment

    print( f"After {duration} years, at {interest}% {rate} interest \
your initial investment of {amount} Pounds \
is worth {total_investment} Pounds." )

#Data collection for bond calcuation

elif user_entry == "bond" or user_entry == "BOND" or user_entry == "Bond":
        house_value=int(input("please enter the value of the house "))
        int_rate=int(input("please enter the interest rate "))
        repayment=int(input("please enter the number of months for repayment "))

    #Calculate the monthly bond repayment

        bond_interest = (int_rate/100)/12
        monthly_repayment = round( (bond_interest * house_value) / 
                          (1 - math.pow((1 + bond_interest), (-repayment))), 2)

#Output the monthly repayment amount

        print(f"For a house value of {house_value} Pounds, at {int_rate}% interest \
the monthly repayment is {monthly_repayment} Pounds. ")

#Error message if investment or bond not entered

else:
    print("Invalid investment type. \
    Please enter investment or bond to proceed.")