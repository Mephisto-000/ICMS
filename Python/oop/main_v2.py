# 使用字典來存放帳戶
from Account_v0 import*

# 以一個空的帳戶串列為起始
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

# 從使用者取得資料來建立其他帳戶：
print()
userName = input('What is the name for the new user account ? ')
userBalance = input('What is the starting balance for this account ? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account ? ')
newAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = newAccount

# 顯示新建立的帳戶
print("Created new account, account number is:", newAccountNumber)
accountsDict[newAccountNumber].show()

# 存 100 元到新帳戶
accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is : ", userBalance)
accountsDict[newAccountNumber].show()
