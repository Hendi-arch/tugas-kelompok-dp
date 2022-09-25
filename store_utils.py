import secrets as sc

def title(title="-", symbol="=", left_count=25, right_count=25):
    return f"{symbol*left_count} {title} {symbol*right_count}"


def lines(symbol='=', length=100):
    return symbol*length

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