import requests

poke_list = []


def poke_parser(pokemon_name):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_name.lower())
    if response.status_code == 200:
        pokemon_info = response.json()
        for info, value in pokemon_info.items():
            if info == 'species':
                for key, value2 in value.items():
                    if key == 'name':
                        poke_list.append(value2.capitalize())
            elif info == 'id':
                poke_list.append(value)
            elif info == 'types':
                poke_type = ''
                type_list = []
                for index in pokemon_info[info]:
                    for key3, value3 in index.items():
                        if key3 == 'type':
                            for key4, value4 in value3.items():
                                if key4 == 'name':
                                    type_list.append(value4.capitalize())
                for index in range(len(type_list)):
                    value = type_list[index]
                    if index < 1:
                        poke_type += value
                    else:
                        poke_type += '/{}'.format(value)
                poke_list.append(poke_type)
            elif info == 'height':
                poke_list.append(value)
            elif info == 'weight':
                poke_list.append(value)
            elif info == 'sprites':
                for key7, value7 in value.items():
                    if key7 == 'other':
                        for key8, value8 in value7.items():
                            if key8 == 'official-artwork':
                                for key9, value9 in value8.items():
                                    if key9 == 'front_default':
                                        poke_list.append(value9)
            elif info == 'game_indices':
                try:
                    for key5, value5 in pokemon_info[info][0].items():
                        if key5 == 'version':
                            for key6, value6 in value5.items():
                                if key6 == 'name':
                                    if value6 == 'blue' or value6 == 'red' or value6 == 'yellow':
                                        poke_list.append('Red/Blue/Yellow')
                                    elif value6 == 'silver' or value6 == 'gold' or value6 == 'crystal':
                                        poke_list.append('Gold/Silver/Crystal')
                                    elif value6 == 'sapphire' or value6 == 'ruby' or value6 == 'emerald':
                                        poke_list.append('Ruby/Sapphire/Emerald')
                                    elif value6 == 'diamond' or value6 == 'pearl' or value6 == 'platinum':
                                        poke_list.append('Diamond/Pearl/Platinum')
                                    elif value6 == 'black' or value6 == 'white':
                                        poke_list.append('Black/White')
                                    elif value6 == 'x' or value6 == 'y':
                                        poke_list.append('X/Y')
                                    elif value6 == 'sun' or value6 == 'moon':
                                        poke_list.append('Sun/Moon')
                                    elif value6 == 'sword' or value6 == 'shield':
                                        poke_list.append('Sword/Shield')
                except IndexError:
                    poke_list.append('Unknown')
