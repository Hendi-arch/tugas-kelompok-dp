# Modules
from store_profile import StoreProfile
from store_menus import StoreMenus
from user_profile import UserProfile
from store_cart import StoreCart

# Begin program

# Adding space
print("\n")

# Heading program
sp = StoreProfile()
sp.show_profile()

# Adding space
print("\n")

up = UserProfile()
up.ask_username()

# Adding space
print("\n")

# Menus
sm = StoreMenus()
sm.show_main_course()
sm.pick_main_courses()
sm.show_beverage()
sm.pick_beverage()

# Adding space
print("\n")

# User input balance
up.ask_balance()

# Adding space
print("\n")

# Cart
sc = StoreCart(up.get_username(), sm.get_selected_menus(),
               up.get_user_balance())
sc.process()

# Adding space
print("\n")

# End program
