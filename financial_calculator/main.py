# Mark Bishop Financial Calculator

#this is the function for the saving goal calculator 
def savings_goal_func():
    savings_weekly_monthly=0
    if int(input("\nThis is the savings goal calculator, you set an item, how much money it costs, \nhow often you will deposit money, and how much, and we will tell you how long \nit will take to save for it.\n\n1. Continue \n\n2. Go back to menu\n\nEnter the number corresponding to your choice: ")) == 1:

        savings_for=input("What item are you saving for? ")
        savings_goal_amount=float(input("How much money would you like to save up for? $"))
        while savings_weekly_monthly not in [1, 2, 3]:
            savings_weekly_monthly=int(input("How often will you deposit money? weekly(1), bi-weekly(2), or monthly(3) "))
        if savings_weekly_monthly == (1):
            savings_weekly_monthly=('week')
        elif savings_weekly_monthly == (2):
            savings_weekly_monthly=('week')
            savings_goal_amount=(savings_goal_amount*2)
        else:
            savings_weekly_monthly=('month')
        savings_income=float(input("How much money do you plan to deposit each time? $"))
        print('calculating...')
        savings_time=(savings_goal_amount/savings_income)
        print(f"it will take {savings_time} {savings_weekly_monthly}s to save up for your: {savings_for}")
    else:
        print("going back to main menu...")

#this is the function for the compound interest caclulator
def compound_interest_func():
    if int(input("\nThis is the coumpound interest calculator, you enter in your principle amount, \nwhich is the amount you depositit, or the amount you loaned, then you enter your \nanual interest rate, next you enter how many times it compounds per year, finnaly \nyou enter the amount of years you're saving it for, then it will output the interest on that money \n\n1. Continue \n\n2. Go back to menu\n\nEnter the number corresponding to your choice: ")) == 1:
        principle_amount=float(input("What is the principle amount? $"))
        anual_intrest_rate=float(input("what is the anual intrest rate? enter as a decimal: "))
        times_compounded=int(input("How many times is it compounded per year? "))
        time_period=int(input("How many years will it be saved for? "))
        final_amount=principle_amount*(1+anual_intrest_rate/times_compounded)**(times_compounded*time_period)
        print(f"After {time_period} years, the final amount will be {final_amount}")
    else:
        print("going back to main menu...")

#This is the fucntion for the budget allocator calculator
def budget_allocator_func():
    if int(input("Welcome to the Budget Allocator!\nEnter your total budget, divide it into sections, and assign percentages to each.\n\n1. Continue \n\n2. Go back to menu\n\nEnter the number corresponding to your choice: ")) == 1:
        budget=float(input("How much money do you want to budget? $"))
        number_of_items=int(input("how many sections do you want to split your budget into? "))
        budget_list=[]
        for i in range(number_of_items):
            item=input(f"add item {i+1} to the list: ")
            budget_list.append(item)
        while True:
            percentages = []
            for i in range(number_of_items):
                percentage = float(input(f"Assign a % to {budget_list[i]}: "))
                percentages.append(percentage)
                if sum(percentages) > 100:
                    print(f"Warning: Total percentage is {sum(percentages)}%. Please reassign the percentages.")
                    break
            break
        if sum(percentages) < 100:
                    leftover = 100 - sum(percentages)
                    budget_list.append("Leftover")
                    percentages.append(leftover)
        print("\nHere is your budget allocation")
        for i in range(number_of_items+1):
            amount=(percentages[i]/100)*budget
            print(f"\n{budget_list[i]}: ${amount:.2f} ({percentages[i]}%)")
    else:
        print("going back to main menu...")

#this is function for the discount calculator
def discount_calculator_func():
    if int(input("Welcome to the Discount Calculator!\nEnter the original price, the discount percentage, and find out how much you save.\n\n1. Continue \n\n2. Go back to menu\n\nEnter the number corresponding to your choice: ")) == 1:
        original_price=float(input("What was the original price? $"))
        discount_percent=float(input("Enter the dsicount % "))
        discount_amount=(original_price*discount_percent)/100
        final_price=(original_price-discount_amount)
        print(f"You saved ${discount_amount:.2f}, and the final price is ${final_price:.2f}.")
    else:
        print("going back to main menu...")

#this is the function for the tip calculator
def tip_calculator_func():
    if int(input("Welcome to the Tip Calculator!\nEnter the bill amount and the tip percentage, and it will calculate the tip and total.\n\n1. Continue \n\n2. Go back to menu\n\nEnter the number corresponding to your choice: ")) == 1:
        price_amount=float(input("What was the price? $"))
        tip_percent=float(input("What % would you like to tip: "))
        tip_amount=(price_amount*tip_percent)/100
        print(f"For a {tip_percent}% tip, you need to leave ${tip_amount:.2f}")
    else:
        print("going back to main menu...")
    
#this is the main function 
def main():
    services=0 
    print("Welcome to the financial calculator.")
    while True:
        while services not in [1, 2, 3, 4, 5]:
            print("please choose an option")
            print("1. Savings goal calculator")
            print("2. Compound interest calculator")
            print("3. Budget allocator")
            print("4. Discount calculator")
            print("5. Tip calculator")
            services=int(input("Enter the number corresponding to your choice: "))
            if services not in [1, 2, 3, 4, 5]:
                print("Please choose a number 1-5")
        
        else:
            if services==(1):
                savings_goal_func()
            elif services==(2):
                compound_interest_func()
            elif services==(3):
                budget_allocator_func()
            elif services==(4):
                discount_calculator_func()
            elif services==(5):
                tip_calculator_func()
        if int(input("\nWould you like to use any of our other services?\n\n1. Yes\n\n2. No\n\nEnter the number corresponding to your choice: "))==2:
            print("Thank you for using the financial calculator!")
            break
        else:
            services=0 

if __name__=="__main__":
    main()