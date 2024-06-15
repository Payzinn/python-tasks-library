def first():
    violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
    time = 0
    ask = int(input('Сколько песен выбрать: '))
    for i in range(ask):
        song_input = input('Название первой песни: ')
        if song_input in violator_songs:
            time += violator_songs[song_input]
        else:
            print('Этой песни нет')
    
    print('Время звучания: {}'.format(time))


def second():
    data = {
    "address": "0x544444444444",
    "ETH": {
    "balance": 444,
    "totalIn": 444,
    "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
    {
    "fst_token_info": {
    "address": "0x44444",
    "name": "fdf",
    "decimals": 0,
    "symbol": "dsfdsf",
    "total_supply": "3228562189",
    "owner": "0x44444",
    "last_updated": 1519022607901,
    "issuances_count": 0,
    "holders_count": 137528,
    "price": False
    },
    "balance": 5000,
    "totalIn": 0,
    "total_out": 0
    },
    {
    "sec_token_info": {
    "address": "0x44444",
    "name": "ggg",
    "decimals": "2",
    "symbol": "fff",
    "total_supply": "250000000000",
    "owner": "0x44444",
    "last_updated": 1520452201,
    "issuances_count": 0,
    "holders_count": 20707,
    "price": False
    },
    "balance": 500,
    "totalIn": 0,
    "total_out": 0
    }
    ]
    }

    data['ETH']['total_diff'] = 100
    data['tokens'][0]['fst_token_info']['name'] = ('doge')
    data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
    data['tokens'][1]['sec_token_info']['total_price'] = ['total_price']

    for i in data:
        print(i, data[i])


def palindrome():
    def ispoly(string):
        char_dict = {}
        for i_sym in string:
            char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

        odd_count = 0
        for i_value in char_dict.values():
            if i_value % 2 != 0:
                odd_count += 1 

        return odd_count <= 1
    
    text = input('Введите строку: ')
    if ispoly(text):
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')

palindrome()