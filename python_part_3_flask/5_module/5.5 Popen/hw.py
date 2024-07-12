import subprocess

# Запускаем команду echo с переменной
process = subprocess.Popen(["sleep 15 && echo", "Hello"], stdout=subprocess.PIPE)

# Читаем и выводим результат
output, error = process.communicate()
print(output.decode())  