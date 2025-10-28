class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
# Initialize account details and convert interest rate to decimal
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate/100

    def deposit(self, amount):
# deposits an amount from the banks balance and make it the new balance
        self.amount += amount
        return f"Amount after deposit: ${self.amount:.2f}"
    def withdraw(self, amount):
# withdraws an amount from the banks balance and make it the new balance
        self.amount -= amount
        return f"Amount after withdraw: ${self.amount:.2f}"
    def balance(self):
# returns account balance
        return f"Balance amount: ${self.amount:.2f}"
    def adj_interest(self, adj_rate):
# converts new interest rate to a decimal and assigns it to the interest rate
        self.interest_rate = adj_rate / 100
        return f"Interest rate adjusted to {self.interest_rate*100:.2f}%"
    def calc_interest(self, days):
# calculate interest rate over any given number of days and add it to the account's balance
        interest_earned = self.amount * (self.interest_rate/365) * days
        self.amount += interest_earned
        return f"After {days} days, interest earned: ${interest_earned:.2f}"

    def __str__(self):
# display the info
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")
# make a test bank account for testing
def test_bank_acct():
    bank1 = BankAcct("Eduardo Ramirez", 1132123, 3000, 3.4)
    print(bank1)
    print("-"*45)
    print(bank1.deposit(850))
    print(bank1.withdraw(1700))
    print(bank1.adj_interest(4.5))
    print(bank1.calc_interest(45))
    print("-"*45)
    print(bank1.balance())
# run the test function
test_bank_acct()