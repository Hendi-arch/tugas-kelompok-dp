from typing import Tuple
from store_utils import title
from store_product import StoreProduct


class StoreMenus:
    def __init__(self, selected_menus: list = []):
        self.__main_courses = [
            StoreProduct(1, "Turkey Salad Sandwich", 100000, "🥗"),
            StoreProduct(2, "Chicken Nodle", 200000, "🍜"),
            StoreProduct(3, "Salmon Salad", 300000, "🍣"),
            StoreProduct(4, "Barbeque Chicken Chop", 177192, "🥓"),
            StoreProduct(5, "Basil Roasted Chicken", 177192, "🐔")
        ]
        self.__beverages = [
            StoreProduct(6, "Milk", 88000, "🥛"),
            StoreProduct(7, "Tea", 50000, "🧋"),
            StoreProduct(8, "Coffee", 30000, "☕"),
            StoreProduct(9, "Sparkling drinks", 99999, "🥂"),
            StoreProduct(10, "Juices", 10000, "🧃")
        ]
        self.__selected_menus = selected_menus

    def show_main_course(self):
        print(title("Main Courses"))
        print('\n')
        for product in self.__main_courses:
            print(f"{product.get_product_id()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()))

    def show_beverage(self):
        print('\n')
        print(title("Beverages"))
        print('\n')
        for product in self.__beverages:
            print(f"{product.get_product_id()}. {product.get_product_name()} - Rp. " +
                  "{:,.2f}".format(product.get_price()))

    def get_selected_menus(self):
        return self.__selected_menus

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
            filter(lambda item: item.get_product_id() == menu_id, self.__main_courses))
        if len(selected_menu) > 0:
            print(f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()}")
            self.__selected_menus.append(selected_menu[0])
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
            filter(lambda item: item.get_product_id() == menu_id, self.__beverages))
        if len(selected_menu) > 0:
            print(f"Added to cart : {selected_menu[0].get_product_name()} {selected_menu[0].get_icon()}")
            self.__selected_menus.append(selected_menu[0])
            self.pick_beverage()
        elif menu_id == 0:
            print("Done.")
        elif len(selected_menu) == 0:
            print("Menu not found, please choose correctly.")
            self.pick_beverage()
