#This is the in class exercise from CIS3145 called Calculate Pay App by James Porter completed 1/29/2021

def main():
    # Define the tips
    print()
    TIP_FIFTEEN = 15
    TIP_TWENTY = 20
    TIP_TWNY_FIVE = 25
    
    
# Ask for mealCost input
# Define the Hours variable and get input from user
    mealCost = float(input("Enter the cost of your meal as a whole number with only two decimals : "))
    round(mealCost,2)
    print("You input a meal cost of : ", mealCost)
    print()
    print("Please enter a tip value for your meal cost.")
    print('='*60)
    
# Create a While loop to check various tip categories against mealCost
    while not mealCost == 0.123456:
        print()

        yourChoice = int(input("[15%]?,[20%]?,[25%]? : "))#Tips are 15, 20, and 25
        float(yourChoice)
        
        if yourChoice == 15:
            TIP_FIFTEEN = 15
        elif yourChoice == 20:
            TIP_TWENTY = 20
        elif yourChoice == 25:
            TIP_TWNY_FIVE = 25

        
    
    # Calculate total cost of the meal with tip
        realTip = 0
        mealTotal = 0
        float(realTip)
        
    # use tip variables as constants
        realTip = mealCost * ( yourChoice / 100 )
    #more math
        mealTotal = realTip + mealCost

    # Print output    
        print("The total price of your tip is : ",'$', round(realTip,2))
    
    # Ask for Hours input
        print("The total cost of your meal is now : ",'$', round(mealTotal,2))
        print()
        print('='*30,'NEXT','='*30)
    
    # Get input from user
        mealCost = float(input("Enter the cost of your meal as a whole number with only two decimals : "))
if __name__ == "__main__":
    main()
    
