class StoreCart:
    def __init__(self, username: str, selected_menus: list, user_balance: float):
        self.__username = username
        self.__selected_menus = selected_menus
        self.__user_balance = user_balance

    def get_username(self):
        return self.__username
    
    def get_selected_menus(self):
        return self.__selected_menus
    
    def get_user_balance(self):
        return self.__user_balance
    
    def process(self):
        print()
