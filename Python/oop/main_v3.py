# 建立互動式功能選單，來測試建立的帳戶字典
from Account_v0 import*

accountsDict = {}
nextAccountNumber = 0



t1 = Account('Joe', 100, 'JoesPassword')
t1AccountNumber = nextAccountNumber
accountsDict[t1AccountNumber] = t1
print("Joe's account number is:", t1AccountNumber)
nextAccountNumber = nextAccountNumber + 1

t2 = Account('Mary', 12345, 'MaryPassword')
t2AccountNumber = nextAccountNumber
accountsDict[t2AccountNumber] = t2
print("Mary's account number is:", t2AccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[t1AccountNumber].show()
accountsDict[t2AccountNumber].show()
print()

# 對不同的帳戶呼叫一些方法來進行相關操作
print('Calling methods of the two accounts ...')
accountsDict[t1AccountNumber].deposit(50, 'JoesPassword')
accountsDict[t2AccountNumber].withdraw(3345, 'MarysPassword')
accountsDict[t2AccountNumber].deposit(100, 'MarysPassword')

accountsDict[t1AccountNumber].show()
accountsDict[t2AccountNumber].show()


while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0] # 抓取第一個字母
    print()

    if action == 'b':
        print("*** Get Balance ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the password: ")
        tAccount = accountsDict[userAccountNumber]
        theBalance = tAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is:", theBalance)

    elif action == 'd':
        print("*** Deposit ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password: ")
        tAccount = accountsDict[userAccountNumber]
        theBalance = tAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print("Your new balance is:", theBalance)

    elif action == 'o':
        print("*** Open Account ***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input("What is the starting balance for this account? ")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the password you want to use for this account? ")
        tAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = tAccount
        print("Your new account number is:", nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == 's':
        print("Show")
        for userAccountNumber in accountsDict:
            tAccount = accountsDict[userAccountNumber]
            print("     Account number:", userAccountNumber)
            tAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print("*** Withdraw ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input("Please enter the amount to withdraw: ")
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input("Please enter the password: ")
        tAccount = accountsDict[userAccountNumber]
        theBalance = tAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print("Withdraw:", userWithdrawalAmount)
            print("Your new balance is:", theBalance)

    else:
        print("Sorry, that was not a valid action. Please try again.")

print("Done")
