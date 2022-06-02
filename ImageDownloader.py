import urllib.request


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
