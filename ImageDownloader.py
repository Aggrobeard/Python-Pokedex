import urllib.request
import PIL.Image
import os
import PokeParser

"""ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']"""
ASCII_CHARS = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 3
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//23] for pixel in pixels])
    return characters


def dl_png(url, file_path):
    file_name = 'pokepic'
    full_path = (file_path + file_name + '.png')
    urllib.request.urlretrieve(url, full_path)


def create_art(file_name):
    url = PokeParser.poke_list[4]
    dl_png(url, 'downloads/' + file_name)
    path = 'downloads/pokepicpokepic.png'
    image = PIL.Image.open(path)

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    new_width = 100
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    os.remove('downloads/pokepicpokepic.png')
