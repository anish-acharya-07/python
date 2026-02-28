#log in
#sign up

#withdraw
#deposit
#balance_inquiry
#transfer_balance
#account_deletion

#account creation / login to account

def log_in():
    pass

def sign_up():
    pass

#banking services

def withdraw():
    pass

def deposit():
    pass

def balance_inquiry():
    pass

def transfer_balance():
    pass

def account_deletion():
    pass


print("\n")
print("*******************WELCOME TO OUR BANK*******************")
print("\n")

while True:

    while True :

        account = input("do you have an existing bank account in our bank (y/n) ? : ").lower()

        if account == "y" :
            pass
            break
        elif account =="n" :
            pass
            break
        else :
            print("invalid..")
            print("try again \n")



    print("\n")
    end_or_continue = input("do you want to continue this program ? (y/n) : ").lower()
    if end_or_continue != "y" :
        print("exiting....")
        break

