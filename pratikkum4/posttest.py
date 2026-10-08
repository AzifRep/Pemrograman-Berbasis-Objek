class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address

    def getAccounts(self):
        print("Nama Bank: ", self.code, "Alamat: ", self.address)

class Customer:
    def __init__(self, name, address, dob, card_number, pin, accounts=None):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin
        self.accounts = accounts if accounts is not None else []

    def verifyPassword(self, input_pin):
        return self.pin == input_pin

class Account:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Saldo tidak cukup!")

class ATMTransaction:
    def __init__(self, transaction_id, date, trans_type, amount, post_balance):
        self.transaction_id = transaction_id
        self.date = date
        self.type = trans_type
        self.amount = amount
        self.post_balance = post_balance

    def modifies(self, account):
        print("Transaksi", self.type, "sebesar", self.amount, "berhasil. Saldo sekarang:", account.balance)

class ATM:
    def __init__(self, location, managedby):
        self.location = location
        self.managedby = managedby

    def checkBalance(self, account):
        print("Saldo Akun", account.number, ":", account.balance)

    def deposit(self, account, amount):
        account.deposit(amount)
        transaksi = ATMTransaction(101, "24-09-2026", "Deposit", amount, account.balance)
        transaksi.modifies(account)

    def withdraw(self, account, amount):
        account.withdraw(amount)
        transaksi = ATMTransaction(102, "24-09-2026", "Withdraw", amount, account.balance)
        transaksi.modifies(account)

bank1 = Bank("BCA", "Purwokerto")
account1 = Account(112233, 1000000)
customer1 = Customer("Budi", "Purwokerto", "15-05-2004", "1234567890", "1234", [account1])
atm1 = ATM("Kampus", bank1.code)
transaksi1 = ATMTransaction(101, "24-09-2026", "Deposit", 500000, 1500000)

bank1.getAccounts()
print("Nama Nasabah :", customer1.name, "| Verifikasi PIN :", customer1.verifyPassword("1234"))
atm1.checkBalance(account1)
transaksi1.modifies(account1)
