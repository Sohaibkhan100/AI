import random
securityPin = [8523,1253,7856,1253,7856]
accounts=[424242424242,535353535353,868686868686,757575757575,434343434343,]

def AccountInfo():
    accountNumber = int(input("enter your account number = "))
    for i in accounts:
        if accountNumber == i:
            print(i)
            widrawMoney()
            break
        else:
            print("you dont have any account please enter your information to open your account")
            OpenAccount()
            break


def OpenAccount():
    name = (input("enter your account name = "))
    CNICNumber = int(input("enter your CNIC number = "))
    type = (input("do you want to open current account or savings? = "))
    pin = int(input("set your pin  4 digit = "))
    securityPin.append(pin)
    newAccountNumber = random.sample(range(0, 1000000000000), 1)
    accounts.append(newAccountNumber)
    print(f"{name}your account is succesfully opened and your account number is {newAccountNumber}")
    deposit()
     

def widrawMoney():
    enterAmount = float(input("enter amount = "))
    pin =int(input("enter your 4 digit pin = "))
    print("money withdraw succesfully")


def deposit():
    accountNumber = int(input("enter your account number = "))
    enterAmount = float(input("enter amount to deposit= "))
    pin = int(input("set your pin  4 digit = "))
    print("amount deposit succesfully")
    AccountInfo()


    
AccountInfo()


    

