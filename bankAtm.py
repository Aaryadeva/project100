class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def balance(self):
        print("your balance is 1000")
    def withdrawl(self,amount):
        new_amount=1000-amount
        print("withdrawn amount: "+str(amount) +" balance remaining is "+ str(new_amount))

def main():
    cardNumber=input("enter your card number: ")
    pinNumber=input("enter your pin number: ")
    newUser=atm(cardNumber,pinNumber)
    print("choose what you want to do ")
    print("1-check your balance   2-withdrawl")
    perform=int(input("enter activity number : "))
    if (perform==1):
        newUser.balance()
    elif (perform==2):
        amount=int(input("enter the amount: "))
        newUser.withdrawl(amount)
    else:
        print("please enter a valid number")

main()