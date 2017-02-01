def account():
    def deposit(amount):
        if amount > 100000000:
            return "!!! Invalid Amount !!!"
        else:
            bank["bal"] += amount
            return str(amount) + " Deposited.\n" + str(bank["Balance"]())

    def withdraw(amount):
        if amount > bank["bal"]:
            return "!!! Amount exceeds the balance !!!"
        else:
            bank["bal"] -= amount
            return str(amount) + " Withdrawn.\n" + str(bank["Balance"]())

    def balance():
        return "Balance= " + str(bank["bal"])

    bank = {"bal": 0,
            "Balance": balance,
            "Deposit": deposit,
            "Withdraw": withdraw}

    return bank


bnk = account()
print(bnk["Balance"]())
print()
print("Withdrawing 100.\n" + bnk["Withdraw"](100))
print()
print(bnk["Deposit"](1000))
print()
print(bnk["Withdraw"](999))
