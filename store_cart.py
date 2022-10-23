import store_utils as su
import pandas as pd
from tabulate import tabulate


class StoreCart:

    def __init__(self,
                 username: str,
                 user_balance: float,
                 total_price_product: float,
                 selected_menus: dict = {}):
        self.__init_attr(username, user_balance, total_price_product,
                         selected_menus)

    def __init_attr(self,
                    username: str,
                    user_balance: float,
                    total_price_product: float,
                    selected_menus: dict = {}):
        self.__username: str = username
        self.__price_discount: float = 0
        self.__user_balance: float = user_balance
        self.__selected_menus: dict = selected_menus
        self.__user_balance_minus_total_price: float = 0
        self.__total_price_minus_total_discount: float = 0
        self.__total_price_product: float = total_price_product

    def __frame_builder(self, data_frame: dict):
        frame = pd.DataFrame.from_dict(data_frame).set_index("No")
        print(tabulate(frame, headers='keys', tablefmt='fancy_grid'))

    def __show_invoice_order(self):
        invoice_order_title = su.title("Invoice Order")
        purchased_items_title = su.title("Purchased items",
                                         left_count=10,
                                         right_count=10)
        data_frame: dict = {"No": [], "Item": [], "Price": [], "Quantity": []}

        print(invoice_order_title)
        print('\n')
        print(purchased_items_title)
        print('\n')
        for index, product in enumerate(self.__selected_menus.values()):
            data_frame["No"].append(index + 1)
            data_frame["Item"].append(f"{product.get_product_name()}")
            data_frame["Price"].append("Rp. " +
                                       "{:,.2f}".format(product.get_price()))
            data_frame["Quantity"].append(product.get_qty())

        self.__frame_builder(data_frame)
        print('\n')
        print(su.lines(length=len(purchased_items_title)))
        print('\n')
        print("Total                    : Rp. " +
              "{:,.2f}".format(self.__total_price_product))
        print("Discount                 : Rp. " +
              "{:,.2f}".format(self.__price_discount))
        print("Total Price Discount     : Rp. " +
              "{:,.2f}".format(self.__total_price_minus_total_discount))
        print("Cash                     : Rp. " +
              "{:,.2f}".format(self.__user_balance))
        print("Change Money             : Rp. " +
              "{:,.2f}".format(self.__user_balance_minus_total_price))

    def process_order(self):
        if self.__total_price_product > 0:
            # Price and discount validation
            self.__price_discount = su.get_price_discount(
                self.__total_price_product)

            if self.__price_discount > 0:
                self.__total_price_minus_total_discount = self.__total_price_product - \
                    self.__price_discount
                self.__user_balance_minus_total_price = self.__user_balance - \
                    self.__total_price_minus_total_discount

            # User balance validation
            if self.__price_discount <= 0:
                self.__user_balance_minus_total_price = self.__user_balance - \
                    self.__total_price_product

            # Show invoice order
            self.__show_invoice_order()
        else:
            print(f"Hi {self.__username}, you didn't order anything.")
