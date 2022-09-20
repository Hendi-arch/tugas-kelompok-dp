from store_product import StoreProduct
import store_utils as su


class StoreCart:
    def __init__(self, username: str, user_balance: float, total_price_product: float, selected_menus: list = []):
        self.__username = username
        self.__selected_menus = selected_menus
        self.__user_balance = user_balance
        self.__total_price_product = total_price_product
        self.__total_price_minus_total_discount = 0
        self.__user_balance_minus_total_price = 0

    def get_username(self):
        return self.__username

    def get_selected_menus(self):
        return self.__selected_menus

    def get_user_balance(self):
        return self.__user_balance

    def get_total_price_product(self):
        return self.__total_price_product

    def get_change(self):
        return self.__user_balance

    def process_order(self):
        # Price and discount validation
        price_discount = su.get_price_discount()
        if price_discount > 0:
            self.__total_price_minus_total_discount = self.__total_price_product - price_discount

        # User balance validation
        self.__user_balance_minus_total_price = self.__user_balance - self.__total_price_product

        # Show invoice order
        self.show_invoice_order()

    def show_invoice_order(self):
        print(su.title("Invoice Order"))
        print('\n')
        print(su.title("Purchased items", left_count=10, right_count=10))
        print('\n')
        for product in self.__selected_menus:
            print(f"{product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()))
        print('\n')
        print("Total                    : " + "{:,.2f}".format(self.__total_price_product))
        print("Total Price Discount     : " + "{:,.2f}".format(self.__total_price_minus_total_discount))
        print("Cash                     : " + "{:,.2f}".format(self.__user_balance))
        print("Change Money             : " + "{:,.2f}".format(self.__user_balance_minus_total_price))
