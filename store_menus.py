from store_utils import gen_product_id, title, get_truly_words
from store_product import StoreProduct


class StoreMenus:
    def __init__(self):
        self.__init_attr()
        
    def __init_attr(self):
        self.__main_courses = [
            StoreProduct(1, "Turkey Salad Sandwich",
                         100000, "🥗", gen_product_id()),
            StoreProduct(2, "Chicken Nodle", 200000, "🍜", gen_product_id()),
            StoreProduct(3, "Salmon Salad", 300000, "🍣", gen_product_id()),
            StoreProduct(4, "Barbeque Chicken Chop",
                         177192, "🥓", gen_product_id()),
            StoreProduct(5, "Basil Roasted Chicken",
                         177192, "🐔", gen_product_id())
        ]
        self.__beverages = [
            StoreProduct(1, "Milk", 88000, "🥛", gen_product_id()),
            StoreProduct(2, "Tea", 50000, "🧋", gen_product_id()),
            StoreProduct(3, "Coffee", 30000, "☕", gen_product_id()),
            StoreProduct(4, "Sparkling drinks", 99999, "🥂", gen_product_id()),
            StoreProduct(5, "Juices", 10000, "🧃", gen_product_id())
        ]
        self.__selected_menus = {}
        self.__total_price_product = 0

    def __user_input(self, caption: str):
        result = input(caption)
        return result

    def __show_current_order(self):
        if len(self.__selected_menus) > 0:
            print('\n')
            print(title("Your current order :", left_count=15, right_count=15))
            for order in self.__selected_menus.values():
                qty_product = f"( x{order.get_qty()} )" if order.get_qty(
                ) > 1 else ""

                print(f"{order.get_product_name()} - Rp. " +
                      "{:,.2f}".format(order.get_price()) + f" {order.get_icon()}" + f" {qty_product}")

    def show_main_course(self):
        print(title("Main Courses"))
        print('\n')
        for product in self.__main_courses:
            print(f"{product.get_index()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()) + f" {product.get_icon()}")

    def show_beverage(self):
        print(title("Beverages"))
        print('\n')
        for product in self.__beverages:
            print(f"{product.get_index()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()) + f" {product.get_icon()}")

    def get_selected_menus(self):
        return self.__selected_menus

    def get_total_price_product(self):
        return self.__total_price_product

    def show_pick_hint(self):
        print('\n')
        print("You can select more than one menu above by typing the number in the menu.")
        print("Type 0 if you want to complete the order.")
        self.__show_current_order()
        print('\n')

    def pick_main_courses(self):
        try:
            menu_id = int(self.__user_input("Choose your Main Course : "))
        except:
            print('\n')
            print("Menu not found, please choose correctly.")
            self.pick_main_courses()
            return

        selected_menu = list(
            filter(lambda item: item.get_index() == menu_id, self.__main_courses))

        if len(selected_menu) > 0:
            while True:
                try:
                    order_qty = int(input(
                        f"Order quantity for {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()} : "))

                    if order_qty > 0:
                        print('\n')
                        break
                    else:
                        print('\n')
                        print("Sorry, the minimum order quantity is one.")
                        print('\n')
                except:
                    print('\n')
                    print("Your input is invalid.")
                    print('\n')

            print(
                f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()} ( x{order_qty} )")
            print('\n')

            menu_exist = list(filter(lambda item: item.get_product_id(
            ) == selected_menu[0].get_product_id(), self.__selected_menus.values()))

            if len(menu_exist) <= 0:
                selected_menu[0].set_qty(order_qty)
                self.__selected_menus[selected_menu[0].get_product_id(
                )] = selected_menu[0]
            else:
                menu_exist[0].set_qty(menu_exist[0].get_qty() + order_qty)
                self.__selected_menus[menu_exist[0].get_product_id(
                )] = menu_exist[0]

            self.__total_price_product += selected_menu[0].get_price() * \
                order_qty

            self.show_main_course()
            self.show_pick_hint()
            self.pick_main_courses()
        elif menu_id == 0:
            print("Done.")
        elif len(selected_menu) == 0:
            print("Menu not found, please choose correctly.")
            self.show_pick_hint()
            self.pick_main_courses()

    def pick_beverage(self):
        try:
            menu_id = int(input("Choose your Beverage : "))
        except:
            print('\n')
            print("Menu not found, please choose correctly.")
            self.pick_beverage()
            return

        selected_menu = list(
            filter(lambda item: item.get_index() == menu_id, self.__beverages))

        if len(selected_menu) > 0:
            while True:
                try:
                    is_no_drinks: bool = False
                    order_qty = int(input(
                        f"Order quantity for {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()} : "))

                    if order_qty > 0:
                        print('\n')
                        break
                    else:
                        answer: str = str(
                            input("Are you sure you don't want to order a drink ? "))

                        if answer.lower() in get_truly_words():
                            is_no_drinks = True
                            print('\n')
                            break
                        else:
                            is_no_drinks = False
                            print('\n')
                except:
                    print('\n')
                    print("Your input is invalid.")
                    print('\n')

            if is_no_drinks:
                print("Done.")
            else:
                print(
                    f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()} ( x{order_qty} )")
                print('\n')

                menu_exist = list(filter(lambda item: item.get_product_id(
                ) == selected_menu[0].get_product_id(), self.__selected_menus.values()))

                if len(menu_exist) <= 0:
                    selected_menu[0].set_qty(order_qty)
                    self.__selected_menus[selected_menu[0].get_product_id(
                    )] = selected_menu[0]
                else:
                    menu_exist[0].set_qty(menu_exist[0].get_qty() + order_qty)
                    self.__selected_menus[menu_exist[0].get_product_id(
                    )] = menu_exist[0]

                self.__total_price_product += selected_menu[0].get_price() * \
                    order_qty

                self.show_beverage()
                self.show_pick_hint()
                self.pick_beverage()
        elif menu_id == 0:
            print("Done.")
        elif len(selected_menu) == 0:
            print("Menu not found, please choose correctly.")
            self.show_pick_hint()
            self.pick_beverage()
