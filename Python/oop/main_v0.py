from Account_v0 import*

t1 = Account('Joe', 100, 'JoesPassword')
t2 = Account('Mary', 12345, 'MaryPassword')

t1.show()
t2.show()
print()

print('Calling methods of the two accounts ...')
t1.deposit(50, 'JoesPassword')
t2.withdraw(345, 'MaryPassword')
t2.deposit(100, 'MaryPassword')

t1.show()
t2.show()

# 從使用者取得資料來建立其他帳戶：
print()
userName = input('What is the name for the new user account ? ')
userBalance = input('What is the starting balance for this account ? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account ? ')
newAccount = Account(userName, userBalance, userPassword)

# 顯示新建立的帳戶
newAccount.show()

# 存 100 元到新帳戶
newAccount.deposit(100, userPassword)
userBalance = newAccount.getBalance(userPassword)
print()
print("After depositing 100, the user's balance is : ", userBalance)
newAccount.show()
