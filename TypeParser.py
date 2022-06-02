import requests

poke_by_type = []
move_by_type = []


def type_parser(type_name):
    response = requests.get('https://pokeapi.co/api/v2/type/' + type_name.lower())
    if response.status_code == 200:
        pokemon_info = response.json()
        for info, value in pokemon_info.items():
            if info == 'pokemon':
                for index in pokemon_info[info]:
                    for key, value2 in index.items():
                        if key == 'pokemon':
                            for key2, value3 in value2.items():
                                if key2 == 'name':
                                    poke_by_type.append(value3.capitalize())
            elif info == 'moves':
                for index in pokemon_info[info]:
                    for key4, value5 in index.items():
                        if key4 == 'name':
                            move_by_type.append(value5.capitalize())


def print_pokes(type_name):
    print("List of {} type Pokemon".format(type_name.capitalize()))
    for key, value in enumerate(poke_by_type):
        if key == 0 or key % 5 != 0:
            print(value, end='          ')
        else:
            print(value)


def print_moves(type_name):
    print("List of {} type moves".format(type_name.capitalize()))
    for key, value in enumerate(move_by_type):
        if key == 0 or key % 5 != 0:
            print(value, end='          ')
        else:
            print(value)
