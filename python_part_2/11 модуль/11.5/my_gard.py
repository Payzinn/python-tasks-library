from garden import PotatoGarden

my_garden = PotatoGarden(5)
my_garden.is_grown()

for i in range(3):
    my_garden.grow_all()

my_garden.is_grown()