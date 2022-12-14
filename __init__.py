# Modules
from store_profile import StoreProfile
from store_menus import StoreMenus
from user_profile import UserProfile
from store_cart import StoreCart

# Begin program

while True:
    # Adding space
    print("\n")

    # Heading program
    sp = StoreProfile()
    sp.show_intro_profile()

    # Adding space
    print("\n")

    up = UserProfile()
    up.ask_username()

    # Adding space
    print("\n")

    # Menus
    sm = StoreMenus()
    sm.show_main_course()
    sm.show_pick_hint()
    sm.pick_main_courses()
    print("\n")
    sm.show_beverage()
    sm.show_pick_hint()
    sm.pick_beverage()

    # Adding space
    print("\n")

    # User input balance
    up.ask_balance(sm.get_total_price_product())

    # Cart
    sc = StoreCart(up.get_username(), up.get_user_balance(),
                   sm.get_total_price_product(), sm.get_selected_menus())
    sc.process_order()

    # Adding space
    print("\n")

    # Show outro
    sp.show_outro_profile()

    # Adding space
    print("\n")

    sp.show_intro_profile()

    # Adding space
    print("\n")

    if up.ask_to_shop_again():
        pass
    else:
        print('\n')
        break

# End program
