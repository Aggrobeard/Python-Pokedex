import PokeParser
import os
import ImageDownloader
import PIL.Image
import PIL


class Pokedex:
    def __init__(self):
        self.pokemon_name = PokeParser.poke_list[3]
        self.pokemon_number = PokeParser.poke_list[2]
        self.pokemon_type = PokeParser.poke_list[5]
        self.pokemon_generation = PokeParser.poke_list[0]
        self.pokemon_height = PokeParser.poke_list[1]
        self.pokemon_height_feet = int(PokeParser.poke_list[1] // 3.08)
        self.pokemon_height_inches = int(round(((PokeParser.poke_list[1] / 3.048) - self.pokemon_height_feet) * 12))
        self.pokemon_height_total = '{} Feet, {} Inches'.format(self.pokemon_height_feet, self.pokemon_height_inches)
        self.pokemon_weight = int(round(PokeParser.poke_list[6] * .220462))
        self.pokemon_image = PokeParser.poke_list[4]

    def print_info(self):
        self.create_art(new_width=100)
        print('                                             Name:', self.pokemon_name)
        print('                                               No:', self.pokemon_number)
        print('                                             Type:', self.pokemon_type)
        print('                                           Height:', self.pokemon_height_total)
        print('                                           Weight:', self.pokemon_weight, 'Pounds')
        print('                                       Generation:', self.pokemon_generation)

    def compare_pokes(self, other, third):
        h1 = self.pokemon_height
        h2 = other.pokemon_height
        h3 = third.pokemon_height
        hh1 = self.pokemon_height_total
        hh2 = other.pokemon_height_total
        hh3 = third.pokemon_height_total
        n1 = self.pokemon_name
        n2 = other.pokemon_name
        n3 = third.pokemon_name
        w1 = self.pokemon_weight
        w2 = other.pokemon_weight
        w3 = third.pokemon_weight
        print()
        if h1 < h2 < h3:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between.'.format(n3, hh3, n1, hh1, n2, hh2))
        elif h1 < h3 < h2:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between.'.format(n2, hh2, n1, hh1, n3, hh3))
        elif h1 == h2 < h3:
            print('{} (at {}) is tallest, but {} and {} (at {}) are the same height!'.format(n3, hh3, n1, n2, hh2))
        elif h1 == h3 < h2:
            print('{} (at {}) is tallest, but {} and {} (at {}) are the same height!'.format(n2, hh2, n1, n3, hh3))
        elif h1 == h2 == h3:
            print('{}, {}, and {} (at {}) are all the same height!'.format(n1, n2, n3, hh1))
        elif h1 < h2 == h3:
            print('{} (at {}) is shortest, but {} and {} (at {}) are the same height!'.format(n1, hh1, n2, n3, hh3))
        elif h2 < h1 < h3:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between'.format(n3, hh3, n2, hh2, n1, hh1))
        elif h2 < h3 < h1:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between'.format(n1, hh1, n2, hh2, n3, hh3))
        elif h2 == h3 < h1:
            print('{} (at {}) is tallest, but {} and {} (at {}) are the same height!'.format(n1, hh1, n2, n3, hh3))
        elif h2 < h1 == h3:
            print('{} (at {}) is shortest, but {} and {} (at {}) are the same height!'.format(n2, hh2, n1, n3, hh3))
        elif h3 < h2 < h1:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between.'.format(n1, hh1, n3, hh3, n2, hh2))
        elif h3 < h1 < h2:
            print('{} (at {}) is tallest, {} (at {}) is shortest, '
                  'and {} (at {}) is in between.'.format(n2, hh2, n3, hh3, n1, hh1))
        elif h3 < h1 == h2:
            print('{} (at {}) is shortest, but {} and {} (at {}) are the same height!'.format(n3, hh3, n1, n2, hh2))
        if w1 < w2 < w3:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {} Pounds) is in between.'.format(n3, w3, n1, w1, n2, w2))
        elif w1 < w3 < w2:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {} Pounds) is in between.'.format(n2, w2, n1, w1, n3, w3))
        elif w1 == w2 < w3:
            print('{} (at {} Pounds) is heaviest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n3, w3, n1, n2, w2))
        elif w1 == w3 < w2:
            print('{} (at {} Pounds) is heaviest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n2, w2, n1, n3, w3))
        elif w1 == w2 == w3:
            print('{}, {}, and {} (at {} Pounds) are all the same weight!'.format(n1, n2, n3, w1))
        elif w1 < w2 == w3:
            print('{} (at {} Pounds) is lightest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n1, w1, n2, n3, w3))
        elif w2 < w1 < w3:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {} Pounds) is in between'.format(n3, w3, n2, hh2, n1, w1))
        elif w2 < w3 < w1:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {} Pounds) is in between'.format(n1, w1, n2, w2, n3, w3))
        elif w2 == w3 < w1:
            print('{} (at {} Pounds) is heaviest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n1, w1, n2, n3, w3))
        elif w2 < w1 == w3:
            print('{} (at {} Pounds) is lightest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n2, w2, n1, n3, w3))
        elif w3 < w2 < w1:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {}) is in between.'.format(n1, w1, n3, w3, n2, w2))
        elif w3 < w1 < w2:
            print('{} (at {} Pounds) is heaviest, {} (at {} Pounds) is lightest, '
                  'and {} (at {} Pounds) is in between.'.format(n2, w2, n3, w3, n1, w1))
        elif w3 < w1 == w2:
            print('{} (at {} Pounds) is lightest, but {} and {} (at {} Pounds)'
                  ' are the same weight!'.format(n3, w3, n1, n2, w2))

    def create_art(self, new_width=100):
        url = self.pokemon_image
        file_name = 'pokepic'
        ImageDownloader.dl_png(url, 'images/' + file_name)
        path = 'images/pokepicpokepic.png'
        image = PIL.Image.open(path)
        new_image_data = ImageDownloader.pixels_to_ascii(ImageDownloader.grayify(ImageDownloader.resize_image(image)))
        new_width = 100
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
        print(ascii_image)
        os.remove('images/pokepicpokepic.png')
