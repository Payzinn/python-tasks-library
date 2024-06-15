def first():
    def print_my_tax(tax, *args, **kwargs):
        price_sum = 0
        for i in args:
            price_sum = price_sum + i * tax / 100
        print("Общая сумма с учётом налога: {}".format(price_sum))
        for i_key,i_value in kwargs.items():
            print("{}: {}".format(i_key,i_value))
    tax = int(input("Введите налог: "))
    print_my_tax(tax, 800, 1000, 200, 300, year = 1992, doc_type = "Report", id = 1112224)
first()