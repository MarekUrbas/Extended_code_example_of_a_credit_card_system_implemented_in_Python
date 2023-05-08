class CreditCard:
    def __init__(self, card_number, card_holder, expiration_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.balance = 0.0

    def charge(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print("Transaction successful. Charged $%.2f" % amount)
        else:
            print("Transaction failed. Insufficient balance.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. Deposited $%.2f" % amount)
        else:
            print("Deposit failed. Invalid amount.")

    def check_balance(self):
        print("Current balance: $%.2f" % self.balance)


class CreditCardSystem:
    def __init__(self):
        self.credit_cards = {}

    def create_account(self, card_number, card_holder, expiration_date):
        if card_number not in self.credit_cards:
            new_card = CreditCard(card_number, card_holder, expiration_date)
            self.credit_cards[card_number] = new_card
            print("Account created successfully.")
        else:
            print("Account creation failed. Card number already exists.")

    def make_transaction(self, card_number, amount):
        if card_number in self.credit_cards:
            card = self.credit_cards[card_number]
            card.charge(amount)
        else:
            print("Transaction failed. Card not found.")

    def make_deposit(self, card_number, amount):
        if card_number in self.credit_cards:
            card = self.credit_cards[card_number]
            card.deposit(amount)
        else:
            print("Deposit failed. Card not found.")

    def check_balance(self, card_number):
        if card_number in self.credit_cards:
            card = self.credit_cards[card_number]
            card.check_balance()
        else:
            print("Balance check failed. Card not found.")


# Example usage
system = CreditCardSystem()

# Create accounts
system.create_account("1234567890", "John Doe", "05/25")
system.create_account("0987654321", "Jane Smith", "08/24")

# Make transactions
system.make_transaction("1234567890", 100.0)
system.make_transaction("0987654321", 50.0)

# Make deposits
system.make_deposit("1234567890", 200.0)
system.make_deposit("0987654321", 75.0)

# Check balances
system.check_balance("1234567890")
system.check_balance("0987654321")
