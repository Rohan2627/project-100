class ATM:
    def __init__(user , atm_cardnumber , pinNumber):
        self.u = user
        self.a = atm_cardnumber
        self.o = pinNumber
        

    def showUser(self):
        print("Name of the user --> " , self.u)

    def balanceEnquiry(self):
        print("Your balance is --> ", self.l)

    def CashWithdrawl(self):
        print("Your card number is --> ", self.o)
        print("Amount of cash withdrawn --> ", self.u)


def firstStep():

    step1 = ATM("Rohan")

    step.showUser()
    


firstStep()


