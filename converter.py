import exchange_rates


def convert_rupees_to_usd(rupees):
    return f"{rupees} Rupees == {rupees//exchange_rates.one_usd} usd"

print(convert_rupees_to_usd(4500))

def convert_usd_to_rupees(usd):
    return f"{usd} USD == {usd*exchange_rates.one_usd} rupees"

print(convert_usd_to_rupees(500))