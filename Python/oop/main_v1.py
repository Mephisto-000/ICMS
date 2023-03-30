# 使用串列來存放帳戶
from Account_v0 import*

# 以一個空的帳戶串列為起始
accountsList = []

t1 = Account('Joe', 100, 'JoesPassword')
accountsList.append(t1)
print("Joe's account number is 0")
t2 = Account('Mary', 12345, 'MaryPassword')
accountsList.append(t2)
print("Mary's account number is 1")


accountsList[0].show()
accountsList[1].show()
print()

# 對不同的帳戶呼叫一些方法來進行相關操作
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(3345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

accountsList[0].show()
accountsList[1].show()

# 從使用者取得資料來建立其他帳戶：
print()
userName = input('What is the name for the new user account ? ')
userBalance = input('What is the starting balance for this account ? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account ? ')
newAccount = Account(userName, userBalance, userPassword)
accountsList.append(newAccount) # 新增到帳戶串列內

# 顯示新建立的帳戶
print("Created new account, account number is 2")
accountsList[2].show()

# 存 100 元到新帳戶
accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is : ", userBalance)
accountsList[2].show()

