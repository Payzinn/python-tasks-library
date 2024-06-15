class Monitor:
    name = 'Name'
    matrix = 'VA'
    resolution = 'WQHD'
    frequency = 60

class Headphones:
    name = 'Name'
    sensitivity = 1
    microphone = False

monitor_samsung = Monitor()
monitor_samsung.frequency = 75

monitor_xiaomi = Monitor()
monitor_xiaomi.frequency = 144

print(monitor_xiaomi.frequency)

headphones_sony = Headphones()
headphones_sony.microphone = True

print(headphones_sony.microphone)

monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].microphone = True
