# This program is adapted from https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# Please debug it :)
import sys
from PIL import Image


ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    original_width, original_height = image.size
    aspect_ratio = original_height // original_width
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value // range_width]
                       for pixel_value in pixels_in_image]

    return ''.join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width]
                   for index in range(0, len_pixels_to_chars, new_width)]

    return '\n'.join(image_ascii)


def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print('Unable to open image file {}.'.format(image_filepath))
        print(e)
        return

    print(convert_image_to_ascii(image))


if __name__ == '__main__':
    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)
