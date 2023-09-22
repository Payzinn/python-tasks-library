def first():
    data = dict()
    data['server'] = {
        "host":"127.0.0.1",
        "port":"10"
    }
    data['configuration'] = {
        "ssh":{
            'access':'true',
            'login':'ivan',
            'password':'qwerty'
        }
    }

    print(data['server']['port'])
    data['configuration']['ssh']['login'] = 'Vova'
    print(data['configuration']['ssh']['login'])
    print()
    for i_value in data.values():
        for j_key in i_value:
            print(j_key, i_value[j_key])


def altfirst():
    data = dict()
    print(data.get('server'))
    data['server'] = {
        "host":"127.0.0.1",
        "port":"10"
    }
    if data.get('configuration', {}).get('ssh', {}).get('login', {}):
        print('В структуре уже есть')

    data['configuration'] = {
        "ssh":{
            'access':'true',
            'login':'ivan',
            'password':'qwerty'
        }
    }

    print(data)


def second():
    players_dict = {
        1: {"name":'Vanya','team':'A', 'status':'Rest'},
        2: {"name":'Lena','team':'B', 'status':'Training'},
        3: {"name":'Maxim','team':'C', 'status':'Travel'},
        4: {"name":'Egor','team':'C', 'status':'Rest'},
        5: {"name":'Andrei','team':'A', 'status':'Training'},
        6: {"name":'Sasha','team':'A', 'status':'Rest'},
        7: {"name":'Alina','team':'B', 'status':'Rest'},
        8: {"name":'Masha','team':'C', 'status':'Travel'}
    }

    team_a_members = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'A' and player['status'] == 'Rest'
    ]

    print(team_a_members)

#hometask

def one():
    order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

    incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

    
    result_sum = 0

    for fruit in order:
        cost = incomes.get(fruit,0) * order[fruit]
        result_sum += cost

    print('Итоговая стоимость: {}' .format(result_sum))


def two():
    players_dict = {
        1: {"name":'Vanya','team':'A', 'status':'Rest'},
        2: {"name":'Lena','team':'B', 'status':'Training'},
        3: {"name":'Maxim','team':'C', 'status':'Travel'},
        4: {"name":'Egor','team':'C', 'status':'Rest'},
        5: {"name":'Andrei','team':'A', 'status':'Training'},
        6: {"name":'Sasha','team':'A', 'status':'Rest'},
        7: {"name":'Alina','team':'B', 'status':'Rest'},
        8: {"name":'Masha','team':'C', 'status':'Travel'}
    }

    team_a_members = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'A' and player['status'] == 'Rest'
    ]

    for i in team_a_members:
        print('Команда А: {}'.format(i))

    team_b_members = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'B' and player['status'] == 'Training'
    ]

    for i in team_b_members:
        print('Команда B: {}'.format(i))

    team_c_members = [
        player['name']
        for player in players_dict.values()
        if player['team'] == 'C' and player['status'] == 'Travel'
    ]

    for i in team_c_members:
        print('Команда C: {}'.format(i))


two()
