def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total
final_price = calculate_total(100, 0.05)
print(final_price)