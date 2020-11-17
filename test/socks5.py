
a = '94.00000'
b = 'NT$94'
price = {}


def get_two_float(f_str, n):
    f_str = str(f_str)
    a, b, c = f_str.partition('.')

    c = (c + "0" * n)[:n]
    return ".".join([a, c])


price_unit = a.strip().replace(
    "NT$", "").replace(",", "").replace(" ", "")
price_nt = b.strip().replace(
    "NT$", "").replace(",", "").replace(" ", "")
price_unit = float(price_unit) * 0.97
price_nt = float(price_nt) * 0.97
price["PRICEBREAK"] = '1'.strip()
price["UNITPRICE"] = get_two_float(
    price_unit, 3)
price["EXTENDEDPRICE"] = get_two_float(
    price_nt, 2)
print(price)
