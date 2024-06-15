first_tour_file = open('first_tour.txt', 'r', encoding='utf-8')
content = first_tour_file.read().split('\n')
first_tour_file.close()
k = content[0]
new_list = []
new_list.extend(content[1:-1])

