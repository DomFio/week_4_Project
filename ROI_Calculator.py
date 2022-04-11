class ROI_Calculator:

    def __init__(self, income, expenses,cash_flow):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_on_cash = 0

    def income_calc(self, income):

        rental_income = int(input("\nHow much is the monthly rental income? (number) "))
      



        laundry = input("\nDo you charge for laundry? (yes/no) ")
        for x in laundry:
            if laundry.lower() =='yes':
                laundry_monthly = int(input("\nHow much do you charge for laundry monthly? (number) "))



                break
            elif laundry.lower() == 'no':
                laundry_monthly = 0
                break
            else:
                print("\ninvaid response please say (yes/no) ")
                return self.income_calc
        storage = input("\nDo you charge for storage? (yes/no) ")
        for x in storage:
            if storage.lower() == 'yes':
                storage_monthly = int(input("\nHow much do you charge for storage monthly? "))



                break
            elif storage.lower() == 'no':
                storage_monthly = 0
                break
            else:
                print("\nInvalid response... (yes/no)")
                return self.income_calc()
        misc = int(input("\nHow much do you charge for miscellaneous expenses? (number)(if none enter 0) "))
 
 
 
        self.income = rental_income + laundry_monthly + storage_monthly + misc
        print(f"\nYour total monthly income is ${self.income}.")



    def expense_calc(self, income, expenses):
        tax = int(input("\nHow much are you charged monthly for taxes? (number) "))



        insurance = input("\nDo you have home owners insurance? (yes/no) ")
        for x in insurance:
            if insurance.lower() == 'yes':
                insurance_monthly = int(input("\nHow much are you charged monthly? (number) "))



                break
            elif insurance.lower() == 'no':
                insurance_monthly = 0
                break
            else:
                print("\nInvalid response... (yes or no)")
                return self.expense_calc()
        utilites = int(input("\nHow much are your monthly Utilities? (number) "))



        HOA = input("\nAre you apart of a HOA in your neighborhood? (yes/no) ")
        for x in HOA:
            if HOA.lower() == 'yes':
                HOA_monthly = int(input("\nHow much are you charged monthly? (number) "))



                break
            elif HOA.lower() == 'no':
                HOA_monthly = 0
                break
            else:
                print("\nInvalid response... (yes or no")
                return self.expense_calc()
        lawn = input("\nDo you pay someone for yard maintenance? (yes/no) ")
        for x in lawn:
            if lawn.lower() == 'yes':
                lawn_monthly = int(input("\nHow much are you charged monthly? (number)"))
                break


            elif lawn.lower() == 'no':
                lawn_monthly = 0
                break
            else:
                print("\nInvalid response... (yes/no) ")
                return self.expense_calc()
        vacancy = self.income * .05
        print(f"\nWe will take 5% of monthly income to account for vacancy... ${vacancy} ")
        repairs = 100
        capex = 100
        print("\nWe will take $100 monthly for repairs and $100 for capex.")
        property_management = self.income * .1
        print(f"\nWe will take 10% of monthly income to account for property management... ${property_management}")
        mortage = int(input("\nHow much is your monthly mortage? "))



        self.expenses = tax + insurance_monthly + utilites + HOA_monthly + vacancy + repairs + capex + property_management + mortage + lawn_monthly
        print(f"\nTotal monthly expenses \n${self.expenses}")






    
    def cash_flow_calc(self ,income ,expenses ,cash_flow):
        print(f"\nYour monthly cash flow \n${self.income - self.expenses}")
        self.cash_flow = self.income - self.expenses



    def cash_on_cash_calc(self ,cash_flow):
        down_payment = int(input("\nHow much did you put down for down payment? (number) "))



        closing_cost = int(input("\nHow much was your closing cost? (number) "))



        rehab_budget = int(input("\nHow much is your rehab budget? (number) "))



        other_expenses = int(input("\nOther expenses? (number) "))


        
        total_investment = down_payment + closing_cost + rehab_budget + other_expenses
        print(f"\nYour total investment is ${total_investment}")
        annual_cashflow = self.cash_flow * 12
        print(f"\nYour annual cash flow is ${annual_cashflow}")
        cash_on_cash_ROI = (annual_cashflow / total_investment) * 100
        print(f"\nYour Cash on Cash ROI is {cash_on_cash_ROI}%")

ROI = ROI_Calculator    
def run():
    
    ROI = ROI_Calculator(0, 0, 0)
    ROI.income_calc(0)
    ROI.expense_calc(0, 0)
    ROI.cash_flow_calc(0,0,0)
    ROI.cash_on_cash_calc(0)
    again = input('\nWould you like to calculate another ROI? (yes/no) ')
    for x in again:
        if again.lower() == 'yes':
            run()
        elif again.lower() == 'no':
            break
        else:
            ("\ninvalid input... (yes or no) ")
            return

run()


