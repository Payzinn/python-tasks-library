def first():
    data = [
    {'id':10, 'user': 'Bob'},
    {'id':11, 'user': 'Misha'},
    {'id':12, 'user': 'Anton'},
    {'id':10, 'user': 'Bob'},
    {'id':11, 'user': 'Misha'},
        ]

    unique_data = []

    for i in data:
        data_exists = False
        for m in unique_data:
            if m['id'] == i['id']:
                data_exists = True
                break
        
        if not data_exists:
            unique_data.append(i)

    print(unique_data)

    unique_data_dict = {i['id']: i for i in data}
    print(unique_data_dict.values())
first()

