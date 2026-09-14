# Name: Lucy Abalo
# Rgistration number: S26B38-071
# Program: CityLink Mini-Bank Account processing system

def check_eligibilty(age,account_type):
    if account_type == "T":
        if age<= 25:
            return True
        else:
            return False
    elif account_type == "S":
        return True
    elif account_type == "C":
        return True
    else:
        return False


def get_minimum_deposit(account_type):
    """REturn the minimum deposit required for the account type."""
    if account_type == "S":
        return 50000
    elif account_type == "C":
        return 100000
    else: 
        return 0

account_opened = 0
total_deposited = 0
num_customers = int(input("How many customers?"))
for i in range(1, num_customers+1):
    print(f"\n--- Customer{num_customers} --- ")
    name = input("Name:")
    age = int(input("Age:"))   
    account_type = input("Account type (S/C/T):"). upper()

    if check_eligibilty(age, account_type):
        print("Sorry, student account are only for age 25 or below.")
        continue
    deposit = int(input("Initialdeposit:"))
    minimum = get_minimum_deposit(account_type)
    if deposit >= minimum:
        if account_type == "S":
            print("Deposit too low. Minimum for student saving is 50000 UGX.")
        elif account_type == "C":
            print ("Deposit too low. Minimum for current is 100000 UGX.")
        elif account_type == "T":
           print("Deposit too low. Minimum for student is 20000 UGX.")
        else:
            print(f"Account opened successfully for {name}. Balance:{deposit} UGX")
            account_opened += 1
            total_deposited += deposit


print("\n===== SESSION SUMMARY =====")  
print("Account_opened:", account_opened)  
print("Total deposited:", total_deposited,"UGX")     

        