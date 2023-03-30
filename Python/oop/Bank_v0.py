# Bank 管理著 Account 物件的字典

from Account_v0 import*

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        tAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = tAccount

        # 遞增來為下一個帳號使用
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print("*** Open Account ***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input("What is the starting balance for this account? ")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the password you want to use for this account? ")
        userAccountNumber = self.createAccount(userName, 
                                               userStartingAmount, 
                                               userPassword)
        print("Your new account number is:", userAccountNumber)
        print()

    def closeAccount(self):
        print("*** Close Account ***")
        userAccountNumber = input("What is your account number? ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("What is your password? ")
        tAccount = self.accountsDict[userAccountNumber]
        theBalance = tAccount.getBalance(userPassword)

        if theBalance is not None:
            print("You had", theBalance, "in your account, which is being returned to you.")

            # 從帳戶的字典移除使用者帳戶
            del self.accountsDict[userAccountNumber]
            print("Your account is now closed.")

    def balance(self):
        print("*** Get Balance ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the password: ")
        tAccount = self.accountsDict[userAccountNumber]
        theBalance = tAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is:", theBalance)

    def deposit(self):
        print("*** Deposit ***")
        accountNum = input("Please enter your account number: ")
        accountNum = int(accountNum)
        depositAmount = input("Please enter amount to deposit: ")
        depositAmount = int(depositAmount)
        userAccountPassword = input("Please enter the password: ")
        tAccount = self.accountsDict[accountNum]
        theBalance = tAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print("Your new balance is:", theBalance)

    def show(self):
        print("*** Show ***")
        for userAccountNumber in self.accountsDict:
            tAccount = self.accountsDict[userAccountNumber]
            print("     Account number:", userAccountNumber)
            tAccount.show()

    def withdraw(self):
        print("*** Withdraw ***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userAmount = input("Please enter the amount to withdraw: ")
        userAmount = int(userAmount)
        userAccountPassword = input("Please enter the password: ")
        tAccount = self.accountsDict[userAccountNumber]
        theBalance = tAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print("Withdraw:", userAmount)
            print("Your new balance is:", theBalance)
            