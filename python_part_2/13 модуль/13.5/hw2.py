def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
            yield clear_line_sum


all_sum = 0
for number in file_parser("n.txt"):
    all_sum += number

print("Вариант №2", all_sum)
