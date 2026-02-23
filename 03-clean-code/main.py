def get_department(postal_code: str):
    if (postal_code[0:2] == 20):
        if (postal_code <= "20190"):
            return "2A"
        else:
            return "2B"
    else:
        return postal_code[0:2]


def get_delivery_fees(country: str, poids: float, is_premium: bool, is_urgent: bool):
    if is_premium:
        return 0.0

    if country == "France":
        if poids <= 2.0:
            return 6.99 if is_urgent else 4.99
        else:
            return 9.99 if is_urgent else 7.99
    elif country in ("Belgique", "Luxembourg"):
        if poids <= 2.0:
            return 12.99 if is_urgent else 9.99
        else:
            return 19.99 if is_urgent else 16.99
    else:
        return 29.99



def main():
    # Tests get_department
    print(get_department("29000"))
    print(get_department("77000"))
    print(get_department("01000"))
    print(get_department("20100"))
    print(get_department("20300"))

    # Tests get_delivery_fees
    print(get_delivery_fees("France", 1.0, False, False))
    print(get_delivery_fees("France", 3.0, False, False))
    print(get_delivery_fees("France", 3.0, True, False))
    print(get_delivery_fees("Belgique", 1.0, False, False))
    print(get_delivery_fees("Belgique", 3.0, False, False))
    print(get_delivery_fees("Luxembourg", 1.0, False, False))
    print(get_delivery_fees("Luxembourg", 10.0, False, False))
    print(get_delivery_fees("Angleterre", 10.0, False, False))


if __name__ == "__main__":
    main()
