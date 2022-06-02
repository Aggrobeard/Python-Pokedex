import pokedex
import PokeParser
import TypeParser

print("Hello, I am your Pokedex. The world of pokemon is vast and expansive. It would be almost impossible for a human "
      "brain to \nlearn all available information about Pokemon. That\'s where I come in! I have uploaded a huge "
      "amount of information regarding\nPokemon into my system. If you require any information, simply use one of my "
      "features to search for the answers you need.")
print('')


def print_menu():
    print('What would you like to do?')
    print('     Main Menu:')
    print('     C  - Compare Three Pokemon')
    print('     P1 - Search Pokemon by Name')
    print('     P2 - Search Pokemon by Number')
    print('     T1 - Search Pokemon by Type')
    print('     T2 - Search Moves by Type')
    print('     Q  - Quit\n')


print_menu()
search = input('Please enter a menu option:\n').lower()
menu_options = ['c', 'p1', 'p2', 't1', 't2', 'q']

while search != 'q':
    if search not in menu_options:
        print('I\'m sorry, that is not a valid menu entry.')
        print_menu()
        search = input('Please enter a menu option:\n').lower()
    while search == 'p1':
        try:
            pokemon_name = input('Please enter the name of the Pokemon you wish to view:\n').lower()
            PokeParser.poke_parser(pokemon_name)
            pokemon_obj = pokedex.Pokedex()
            pokedex.Pokedex.print_info(pokemon_obj)
            PokeParser.poke_list = []
            search_again = input("\nWould you like to look up another Pokemon?\nY/N\n").lower()
        except IndexError:
            print('I\'m sorry, that is not a Pokemon. Try again:')
            continue
        if search_again == 'y':
            continue
        elif search_again == 'n':
            print_menu()
            search = input('Please enter a menu option:\n').lower()
            break

    while search == 'p2':
        pokemon_name = input('Please enter the number of the Pokemon you wish to view:\n')
        PokeParser.poke_parser(pokemon_name)
        pokemon_obj = pokedex.Pokedex()
        pokedex.Pokedex.print_info(pokemon_obj)
        PokeParser.poke_list = []
        search_again = input("\nWould you like to look up another Pokemon?\nY/N\n").lower()
        if search_again == 'y':
            continue
        elif search_again == 'n':
            print_menu()
            search = input('Please enter a menu option:\n').lower()
            break

    while search == 't1':
        type_name = input('Please enter the type of Pokemon you wish to view:\n')
        TypeParser.type_parser(type_name)
        TypeParser.print_pokes(type_name)
        TypeParser.move_by_type = []
        TypeParser.poke_by_type = []
        search_again = input("\nWould you like to look up another Type of Pokemon?\nY/N\n").lower()
        if search_again == 'y':
            continue
        elif search_again == 'n':
            print_menu()
            search = input('Please enter a menu option:\n').lower()
            break

    while search == 't2':
        type_name = input('Please enter the type of Moves you wish to view:\n')
        TypeParser.type_parser(type_name)
        TypeParser.print_moves(type_name)
        TypeParser.move_by_type = []
        TypeParser.poke_by_type = []
        search_again = input("\nWould you like to look up another Type of Moves?\nY/N\n").lower()
        if search_again == 'y':
            continue
        elif search_again == 'n':
            print_menu()
            search = input('Please enter a menu option:\n').lower()
            break

    while search == 'c':
        try:
            pokemon_1 = input('Please enter the name or number of the first Pokemon you\'d like to compare\n')
            PokeParser.poke_parser(pokemon_1)
            pokemon_obj1 = pokedex.Pokedex()
            PokeParser.poke_list = []
            pokemon_2 = input('Please enter the name or number of the second Pokemon you\'d like to compare\n')
            PokeParser.poke_parser(pokemon_2)
            pokemon_obj2 = pokedex.Pokedex()
            PokeParser.poke_list = []
            pokemon_3 = input('Please enter the name or number of the third Pokemon you\'d like to compare\n')
            PokeParser.poke_parser(pokemon_3)
            pokemon_obj3 = pokedex.Pokedex()
            PokeParser.poke_list = []
            pokedex.Pokedex.compare_pokes(pokemon_obj1, pokemon_obj2, pokemon_obj3)
        except IndexError:
            print('I\'m sorry, that is not a Pokemon. Try again:')
            continue
        search_again = input('\nWould you like to compare more Pokemon?\nY/N\n').lower()
        if search_again == 'y':
            continue
        elif search_again == 'n':
            print_menu()
            search = input('Please enter a menu option:\n').lower()
