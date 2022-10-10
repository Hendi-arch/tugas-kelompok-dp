from store_utils import gen_product_id


class StoreProduct:

    def __init__(self,
                 index,
                 product_name,
                 price,
                 icon,
                 product_id,
                 category_product,
                 qty=0):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__icon = icon
        self.__index = index
        self.__qty = qty
        self.__category_product = category_product

    def __getitem__(self):
        pass

    def __setitem__(self):
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StoreProduct):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__product_id == other.__product_id and self.__product_name == other.__product_name and self.__price == other.__price and self.__icon == other.__icon and self.__index == other.__index and self.__qty == other.__qty

    def get_product_id(self) -> int:
        return self.__product_id

    def get_product_name(self) -> str:
        return self.__product_name

    def get_price(self) -> int:
        return self.__price

    def get_icon(self):
        return self.__icon

    def get_index(self):
        return self.__index

    def get_qty(self):
        return self.__qty

    def get_category_product(self):
        return self.__category_product

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

    def set_index(self, new_data):
        self.__index = new_data
        return self.__index

    def set_qty(self, new_data):
        self.__qty = new_data
        return self.__qty

    def set_category_product(self, new_data):
        self.__category_product = new_data
        return self.__category_product
