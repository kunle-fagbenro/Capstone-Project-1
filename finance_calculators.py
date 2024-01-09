import math
print()

# Display the message for options for users
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()

# User input requested. Convert any input to lower case.
financial_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
print()



# How to recognise different case types for "Bond" & "Investment"
    
# Request details for P, r & t for the "investment" option
if financial_calculator == "investment": 
    # P (Deposit) input
    P = int(input("Please enter the amount you will be depositing (in British £): "))
    print()
    # r (interest rate) input
    r_user = int(input("Please enter the interest rate(%): ").strip("%"))
    r = r_user/100
    print()
    # t (Time) input
    t = int(input("Please enter the number of years you plan on investing: "))
    print()
    
    # Simple interest calculation
    A_simple_interest = P * (1 + r * t)
    print()
    # Compound interest calculation
    A_compound_interest = P * math.pow ((1 + r), t)
    print()
    
    # Request interest type: simple or compound
    interest = input('Would you want "simple" or "compound" interest: ').lower()
    print()
    
    # Output appropriate display based on interest type selected
        # Simple interest output
    if (interest == "simple") :
        print( f"The total amount you will get back after {t} years at {r_user}% interest rate will be £{A_simple_interest}")
        print()
        # Compound interest output
    elif (interest == "compound") :
        print( f"The total amount you will get back after {t} years at {r_user}% interest rate will be £{A_compound_interest}")
        print()
        # Error message display if neither "simple" or "compound" entered
    else:
        print('Please enter valid interest type: "simple" or "compound".')
        print()
        
# When "bond" selected, request i, P & n details
elif financial_calculator == "bond":
    # P (Present House Value)
    P = int(input("Please enter the present value of the House (British £): "))
    print()
    # i (Monthly interest rate)
    i_user = int(input("Please enter Interest Rate(%): ").strip("%"))
    i = (i_user/100)/12
    print()
    # n (Number of repayment months)
    n = int(input("Please enter the number of months you plan to repay the bond: "))
    print()
    
    # Bond Replayment calculation
    replayment = (i * P) / (1 - (1 + i) ** ( - n))
    
    print(f"The total amount of repayment each month with house value £{P} at {i_user}% interest rate will be £{replayment} for {n} months.")
    print()
    # Error message for incorrect user input
else:
    print("Please enter a valid option: 'Investment' or 'Bond'.")
    print()