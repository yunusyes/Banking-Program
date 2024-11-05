class Banking:
    
    def __init__(self):
        self.balance = 0

    def banking_program_layout(self):
        for i in range(20):
            print("*", end="")
        print("")
        print("  Banking Program")
        for i in range(20):
            print("*", end="")
        print("")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        self.user = input("Enter your choice(1-4): ")
        if self.user == "1":
            for i in range(20):
                print("*", end="")
            print("")
            self.show_balance()
        elif self.user == "2":
            for i in range(20):
                print("*", end="")
            print("")
            self.deposit()
        elif self.user == "3":
            for i in range(20):
                print("*", end="")
            print("")
            self.withdraw()
        elif self.user == "4":
            for i in range(20):
                print("*", end="")
            print("")
            self.exit()
        else:
            print("Invalid")
            self.banking_program_layout()
        
    def show_balance(self):
        print(f"Your balance is ${self.balance}")
        self.banking_program_layout()
        
    def deposit(self):
        try:
            deposit = int(input("Enter an amount to be deposited: "))
            self.balance += deposit
        except ValueError:
            print("Your operation of deposit cannot be continued because you entered invalid information such as characters or decimal numbers")
        self.banking_program_layout()
        
    def withdraw(self):
        try:
            withdraw = int(input("Enter an amount to be withdrawn: "))
            self.balance -= withdraw
        except ValueError: 
            print("Your operation of withdraw cannot be continued because you entered invalid information such as characters or decimal numbers.")
        if self.balance < 0:
            self.balance += withdraw
            print("Your operation of withdraw cannot be continued because you don't have the required amount to withdraw")
        self.banking_program_layout()
        
    def exit(self):
        print("Thank you! Have a nice day!")
        
    
    
def main():
    bp = Banking()
    bp.banking_program_layout()
    
if __name__ == "__main__":
    main()
    
    

