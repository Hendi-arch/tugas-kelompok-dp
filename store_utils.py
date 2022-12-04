import secrets as sc
from typing import List
import pandas as pd
from tabulate import tabulate


def title(title="-", symbol="=", left_count=25, right_count=25):
    return f"{symbol*left_count} {title} {symbol*right_count}"


def lines(symbol='=', length=100):
    return symbol * length


def get_price_discount(total: float = 0) -> float:
    price_discount: float = 0

    if total >= 500000:
        # Eligible for discount 30%
        price_discount = 500000 / 100 * 30
    elif total >= 300000 and total < 500000:
        # Eligible for discount 15%
        price_discount = total / 100 * 15
    else:
        # Not eligible for discount
        pass

    return price_discount


def gen_product_id() -> str:
    return sc.token_hex(8)


def get_truly_words() -> List[str]:
    return [
        'true', '1', 't', 'y', 'yes', 'ok', 'oke', 'okey', 'okay', 'yeah',
        'yup', 'certainly', 'uh-huh', 'ya', 'iya', 'baik', 'iyah', 'yo', 'yah',
        'benar'
    ]


def get_product_action():
    options: list = [
        'add product', 'delete product', 'change product price',
        'change product quantity', 'change product name'
    ]

    for index, option in enumerate(options):
        print(f'{index + 1}. {option.title()}')


def frame_builder(data_frame: dict):
    frame = pd.DataFrame.from_dict(data_frame).set_index("No")
    print(tabulate(frame, headers='keys', tablefmt='fancy_grid'))