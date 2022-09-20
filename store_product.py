class StoreProduct:
    def __init__(self, product_id, product_name, price, icon):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__icon = icon

    def __getitem__(self):
        pass

    def __setitem__(self):
        pass

    def get_product_id(self) -> int:
        return self.__product_id

    def get_product_name(self) -> str:
        return self.__product_name

    def get_price(self) -> int:
        return self.__price
    
    def get_icon(self):
        return self.__icon

    def set_product_id(self, new_data):
        self.__product_id = new_data
        return self.__product_id

    def set_product_name(self, new_data):
        self.__product_name = new_data
        return self.__product_name

    def set_price(self, new_data):
        self.__price = new_data
        return self.__price
    
    def set_icon(self, new_data):
        self.__icon = new_data
        return self.__icon
