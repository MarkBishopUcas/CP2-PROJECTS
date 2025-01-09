# Mark Bishop Financial Calculator

def savings_goal ():
    savings_for=input("What item are you saving for? ")
    savings_goal_amount=int(input("How much money would you like to save up for? "))
    savings_weekly_monthly=int(input("How often will you deposit money? weekly(1), bi-weekly(2), or monthly(3) "))
    if savings_weekly_monthly == (1):
        savings_weekly_monthly=('week')
    elif savings_weekly_monthly == (2):
        savings_weekly_monthly=('week')
        savings_goal_amount=(savings_goal_amount*2)
    else:
        savings_weekly_monthly=('month')
    savings_income=int(input("How much money do you plan to deposit each time? "))
    print('calculating...')
    savings_goal_amount=(savings_goal_amount-current_money)
    savings_time=(savings_goal_amount/savings_income)
    print(f"it will take {savings_time} {savings_weekly_monthly}s to save up for your: {savings_for}")

def main():
    print("Welcome to the financial calculator. Before you begin, when presented with a multiple choice question, please awnser with the number to the left of the option you want to select.")
    current_money=int(input("What is your current ballance? "))
    services=int(input("which of our services would you like to usse? Savings goal calculator(1), Compound interest calculator(2), Budget allocator(3), Discount calculator(4), Tip calculator(5) "))