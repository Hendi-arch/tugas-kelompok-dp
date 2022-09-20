def title(title="-", symbol="=", left_count=25, right_count=25):
    return f"{symbol*left_count} {title} {symbol*right_count}"


def lines(symbol='=', length=100):
    return symbol*length

def is_eligible_for_discount(total: float = 0) -> bool:
    is_eligible: bool = False
    
    if total >= 500000:
        print("Eligible for discount 30%", total)
    elif total >= 300000 and total < 500000:
        print("Eligible for discount 15%", total)
    else:
        print("Not eligible for discount", total)
    
    return is_eligible