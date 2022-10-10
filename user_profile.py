class UserProfile:

    def __init__(self, username: str = "", user_balance: int = 0):
        self.__username = username
        self.__user_balance = user_balance

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username
        return self.__username

    def get_user_balance(self) -> float:
        return self.__user_balance

    def set_user_balance(self, user_balance: float) -> float:
        self.__user_balance = user_balance
        return self.__user_balance

    def ask_username(self):
        print(
            "Hello, welcome to the group 2 store, so that we can know more, may we know the names of sir and madam?"
        )
        while True:
            self.__username = input("Name : ").title()

            if self.__username.lower() == 'admin':
                while True:
                    password = input("Password : ")

                    if password == "1234":
                        print('\n')
                        print(
                            f"Hi {self.__username}, here are the products in store. :)"
                        )
                        break
                    else:
                        print('\n')
                        print('Password does not match!')
                        print('\n')
                break
            else:
                if len(self.__username.strip()) > 0:
                    print('\n')
                    print(
                        f"Hi {self.__username}, here are the menus in our store. :)"
                    )
                    break
                else:
                    print("Sorry, the name cannot be empty.")

    def ask_balance(self, total_price_product: float):
        if total_price_product > 0:
            print("Please input your balance.")
            print("Price to pay : Rp. " +
                  "{:,.2f}".format(total_price_product))

            try:
                self.__user_balance = float(input("Balance : "))
            except:
                print(
                    "Sorry, your balance must be greater than total price product."
                )
                print('\n')
                self.ask_balance(total_price_product)
                return

            if self.__user_balance < total_price_product:
                print(
                    "Sorry, your balance is less than the total price of the product."
                )
                self.set_user_balance(0)
                print('\n')
                self.ask_balance(total_price_product)
            else:
                print('\n')
                print(
                    f"Great {self.__username}, we are processing your order!")
                print("\n")
