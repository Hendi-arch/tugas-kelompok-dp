from store_product import StoreProduct
import store_utils as su


class StoreCart:

    def __init__(self,
                 username: str,
                 user_balance: float,
                 total_price_product: float,
                 selected_menus: dict = {}):
        self.__username = username
        self.__selected_menus = selected_menus
        self.__user_balance = user_balance
        self.__total_price_product = total_price_product
        self.__total_price_minus_total_discount = 0
        self.__user_balance_minus_total_price = 0
        self.__price_discount = 0

    def __show_invoice_order(self):
        invoice_order_title = su.title("Invoice Order")
        purchased_items_title = su.title("Purchased items",
                                         left_count=10,
                                         right_count=10)
        print(invoice_order_title)
        print('\n')
        print(purchased_items_title)
        print('\n')
        for product in self.__selected_menus.values():
            qty_product = f"( x{product.get_qty()} )" if product.get_qty(
            ) > 1 else ""

            print(f"{product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()) +
                  f" {product.get_icon()}" + f" {qty_product}")
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
            print(
                f"Hi {self.__username}, you didn't order anything."
            )
