#BANK MANAGEMENT SYSTEM
#define dictionary to store account informaion
accounts={}
#define fun to create account
def create_account(account_no,initial_balance):
    if account_no in accounts:
        print("Account already exist")
    else:
        accounts[account_no]=initial_balance       
        print("created sucssfully")
#define fun to deposit amount
def deposit(account_no,amount):
    if account_no in accounts:
        accounts[account_no]+=amount
        print("deposit sucessfully")        
    else:
        print("Account not found")    
#define fun to withdraw amount
def withdraw(account_no,amount):
    if account_no in accounts:
        if accounts[account_no]>=amount:
            accounts[account_no]-=amount
            print("withdraw sucessfully")
        else:
            print("insufficient amount")    
    else:
        print("Account not found")    
#define fun to check balance
def check_balance(account_no):
    if account_no in accounts:
        print("Account amount",accounts[account_no])
    else:
        print("Account not found")    
#define fun to save data to file
def save_data():
    with open("accounts.txt","w") as file:
        for account_no,balance in accounts.items():
            file.write(f"{account_no}:{balance}\n")
            print("saved sucessfully")
#define fun to load data
def load_data():
    try:
        with open("accounts.txt","r") as file:
            for line in file:
                account_no,balance=line.strip().split(":")
                accounts[account_no]=float(balance)
                print("load data sucussfully")
    except FileNotFoundError:
        print("no found  data")            



#main fun
load_data()        


while True:
    print("1.Create account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check balance")
    print("5.Save & Exit")

    choice=input("Enter your Choice :")
    if choice=="1":
        account_no=input("Enter account no.")
        try:
            initial_balance=float(input("Enter initial balance"))
            create_account(account_no,initial_balance)
        except ValueError:
            print("invalid no .please enter valid no")    
    elif choice=="2":
        account_no=input("Enter account no.")
        try:
            amount=float(input("enter amount"))
            deposit(account_no,amount)
        except ValueError:
            print("invalid no .please enter valid no")    
    elif choice=="3":
        account_no=input("Enter account no.")        
        try:
            amount=float(input("enter amount"))
            withdraw(account_no,amount)
        except ValueError:
            print("invalid input. please enter valid no.")   
    elif choice=="4":
        account_no=input("Enter account no.")
        check_balance(account_no)        
    elif choice=="5":
        save_data()
        break
    else:
        print("invalid choice.please enter valid choice")    


                

