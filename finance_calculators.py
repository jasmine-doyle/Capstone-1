import math

#printing out initial information for user to pick from
#the programme uses white space to make text more readable
x= " "
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print(f"\ninvestment{2*x}-{2*x}to calculate the amount of interest you'll earn on your investment")
print(f"bond{8*x}-{2*x}to calculate the amount you'll have to pay on a home loan")

#the user chooses between investment and bond
#if input is invalid, the programme will ask again until valid answer is inputted
while True:
    choice = input("\nWhat is your choice?").lower()
    if (choice == "investment") or (choice == "bond"):
        break
    else:
        print("Invalid answer. Please try again.")

#the following code runs if the user inputs interest
#calculating the interest depending on whether the user inputs simple or compound
#displaysthe amount they get back after a given period
if choice == "investment":
    deposit = float(input("\nHow much money are you depositing?"))
    interest_rate = float(input("\nWhat is the interest rate?"))
    r=interest_rate/100
    num_years = int(input("\nHow many years do you plan on investing?"))
    while True:
        interest = input("\nWould you like simple or compound interest?").lower()
        if (interest == "simple") or (interest == "compound"):
            break
        else:
            print("Invalid answer. Please try again")
    if interest == "simple":
        amount = deposit*(1+r*num_years)
    elif interest == "compound":
        amount = deposit*math.pow((1+r),num_years)
    print("\nAfter {} years you will get back £{:.2f}.".format(num_years,amount))

#the following code runs if the user inputs bond
#calculating the amount they have to repay each month
elif choice == "bond":
    value_house = float(input("\nWhat is the present value of the house?"))
    interest_rate = float(input("\nWhat is the interest rate?"))
    monthly_interest_rate = interest_rate/(12*100)
    num_months = int(input("\nHow many months do you plan to take to repay the bond?"))

    repayment = (monthly_interest_rate * value_house)/(1-(1+monthly_interest_rate)**(-num_months))
    print("\nEach month you will have to repay £{:.2f}.".format(repayment))
