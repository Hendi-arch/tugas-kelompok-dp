from store_utils import gen_product_id, title
from store_product import StoreProduct


class StoreMenus:
    def __init__(self, selected_menus: dict = {}):
        self.__main_courses = [
            StoreProduct(1, "Turkey Salad Sandwich", 100000, "🥗", gen_product_id()),
            StoreProduct(2, "Chicken Nodle", 200000, "🍜", gen_product_id()),
            StoreProduct(3, "Salmon Salad", 300000, "🍣", gen_product_id()),
            StoreProduct(4, "Barbeque Chicken Chop", 177192, "🥓", gen_product_id()),
            StoreProduct(5, "Basil Roasted Chicken", 177192, "🐔", gen_product_id())
        ]
        self.__beverages = [
            StoreProduct(1, "Milk", 88000, "🥛", gen_product_id()),
            StoreProduct(2, "Tea", 50000, "🧋", gen_product_id()),
            StoreProduct(3, "Coffee", 30000, "☕", gen_product_id()),
            StoreProduct(4, "Sparkling drinks", 99999, "🥂", gen_product_id()),
            StoreProduct(5, "Juices", 10000, "🧃", gen_product_id())
        ]
        self.__selected_menus = selected_menus
        self.__total_price_product = 0

    def show_main_course(self):
        print(title("Main Courses"))
        print('\n')
        for product in self.__main_courses:
            print(f"{product.get_index()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()) + f" {product.get_icon()}")

    def show_beverage(self):
        print('\n')
        print(title("Beverages"))
        print('\n')
        for product in self.__beverages:
            print(f"{product.get_index()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()) + f" {product.get_icon()}")

    def get_selected_menus(self):
        return self.__selected_menus

    def get_total_price_product(self):
        return self.__total_price_product

    def pick_main_courses(self):
        print('\n')
        print("You can select more than one menu above by typing the number in the menu.")
        print("Type 0 if you want to complete the order.")
        print('\n')

        try:
            menu_id = int(input("Choose your Main Course : "))
        except:
            print("Menu not found, please choose correctly.")
            self.pick_main_courses()
            return

        print('\n')
        selected_menu = list(
            filter(lambda item: item.get_index() == menu_id, self.__main_courses))
        if len(selected_menu) > 0:
            print(f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()}")

            menu_exist = list(filter(lambda item: item.get_product_id(
            ) == selected_menu[0].get_product_id(), self.__selected_menus.values()))
            
            if len(menu_exist) <= 0:
                selected_menu[0].set_qty(selected_menu[0].get_qty() + 1)
                self.__selected_menus[selected_menu[0].get_product_id()] = selected_menu[0]
            else:
                menu_exist[0].set_qty(menu_exist[0].get_qty() + 1)
                self.__selected_menus[menu_exist[0].get_product_id()] = menu_exist[0]

            self.__total_price_product += selected_menu[0].get_price()
            self.pick_main_courses()
        elif menu_id == 0:
            print("Done.")
        elif len(selected_menu) == 0:
            print("Menu not found, please choose correctly.")
            self.pick_main_courses()

    def pick_beverage(self):
        print('\n')
        print("You can select more than one menu above by typing the number in the menu.")
        print("Type 0 if you want to complete the order.")
        print('\n')

        try:
            menu_id = int(input("Choose your Beverage : "))
        except:
            print("Menu not found, please choose correctly.")
            self.pick_beverage()
            return

        print('\n')
        selected_menu = list(
            filter(lambda item: item.get_index() == menu_id, self.__beverages))
        if len(selected_menu) > 0:
            print(
                f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()}")
            
            menu_exist = list(filter(lambda item: item.get_product_id(
            ) == selected_menu[0].get_product_id(), self.__selected_menus.values()))
            
            if len(menu_exist) <= 0:
                selected_menu[0].set_qty(selected_menu[0].get_qty() + 1)
                self.__selected_menus[selected_menu[0].get_product_id()] = selected_menu[0]
            else:
                menu_exist[0].set_qty(menu_exist[0].get_qty() + 1)
                self.__selected_menus[menu_exist[0].get_product_id()] = menu_exist[0]
            
            self.__total_price_product += selected_menu[0].get_price()
            self.pick_beverage()
        elif menu_id == 0:
            print("Done.")
        elif len(selected_menu) == 0:
            print("Menu not found, please choose correctly.")
            self.pick_beverage()
