def get_avg_value(shares, min_p=None, max_p=None):
    sum_prices = 0
    count = 0
    for share in shares:
        price = share.get("price")
        if price is not None and (min_p is None or price >= min_p) and (max_p is None or price <= max_p):
            sum_prices += price
            count += 1
    if count > 0:
        return sum_prices/count
    else:
        print("No appropriate data")

shares = [
 {"name": "AAPL", "price": 150},
 {"name": "GOOGL", "price": 2800},
 {"name": "TSLA", "price": 700},
 {"name": "AMZN", "price": None},
]
print(get_avg_value(shares))
print(get_avg_value(shares, 200, 2000))

