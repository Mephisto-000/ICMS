from Bank_v0 import*


# 建立 Bank 的實例物件
tBank = Bank()


t1AccountNumber = tBank.createAccount('Joe', 100, 'JoesPassword')
print("Joe's account number is:", t1AccountNumber)

t2AccountNumber = tBank.createAccount('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", t2AccountNumber)



while True:
    print()
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    # print("To get bank information, press i")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0] # 題取第一個字母
    print()

    if action == 'b':
        tBank.balance()
    
    elif action == 'c':
        tBank.closeAccount()

    elif action == 'd':
        tBank.deposit()

    # elif action == 'i':
    #     tBank.bankInfo()

    elif action == 'o':
        tBank.openAccount()

    elif action == 's':
        tBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        tBank.withdraw()

    else:
        print("Sorry, that was not a valid action. Please try again.")

print("Done")

