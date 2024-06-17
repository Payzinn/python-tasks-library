import re

form = {"name": "Иванов И.И."}  # Пример данных из формы

pattern = r'\w+ \w{1}.\w{1}'
result = re.match(pattern, str(form.name))

if result:
    print("Строка соответствует формату Иванов И.И.")
else:
    print("Строка не соответствует формату Иванов И.И.")