import sys
import os

clear_console = 'clear' if os.name == 'posix' else 'CLS'

from PIL import Image
from PIL import ImageSequence

def txt_to_ascii_flip(average):
    return_char = '  '
    if average < 255 / 12 * 1:
        return_char = ' @'
    elif average < 255 / 12 * 2:
        return_char = ' $'
    elif average < 255 / 12 * 3:
        return_char = ' #'
    elif average < 255 / 12 * 4:
        return_char = ' *'
    elif average < 255 / 12 * 5:
        return_char = ' !'
    elif average < 255 / 12 * 6:
        return_char = ' ='
    elif average < 255 / 12 * 7:
        return_char = ' ;'
    elif average < 255 / 12 * 8:
        return_char = ' :'
    elif average < 255 / 12 * 9:
        return_char = ' ~'
    elif average < 255 / 12 * 10:
        return_char = ' -'
    elif average < 255 / 12 * 11:
        return_char = ' ,'
    elif average < 255 / 12 * 12:
        return_char = ' .'
    
    return return_char

def txt_to_ascii(average):
    return_char = '  '
    if average < 255 / 12 * 1:
        return_char = ' .'
    elif average < 255 / 12 * 2:
        return_char = ' ,'
    elif average < 255 / 12 * 3:
        return_char = ' -'
    elif average < 255 / 12 * 4:
        return_char = ' ~'
    elif average < 255 / 12 * 5:
        return_char = ' :'
    elif average < 255 / 12 * 6:
        return_char = ' ;'
    elif average < 255 / 12 * 7:
        return_char = ' ='
    elif average < 255 / 12 * 8:
        return_char = ' *'
    elif average < 255 / 12 * 9:
        return_char = ' !'
    elif average < 255 / 12 * 10:
        return_char = ' #'
    elif average < 255 / 12 * 11:
        return_char = ' $'
    elif average < 255 / 12 * 12:
        return_char = ' @'
    
    return return_char

input_path = input('file path: ')

img = Image.open(input_path)
img = img.resize((int(input("x axis size: ")), int(input("y axis size: "))))

flipped = input('do you want to flip the colors (y/n)? ')

if flipped == 'y':
    flipped = True
elif flipped == 'n':
    flipped = False

img = img.convert('RGB')

output = '\n\n'

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel = img.getpixel((y, x))
        average = (pixel[0] + pixel[1] + pixel[2]) / 3
        if flipped:
            output += txt_to_ascii_flip(average)
        else:
            output += txt_to_ascii(average)
    output += '\n'

if not os.path.exists('output/'):
    os.makedirs('output/')

# gets name of file without the folder its in or its extension
filename = input_path.split('/')[-1].split('.')[0]

output_file = open("output/{}.txt".format(filename), 'a')
output_file.write(output)
output_file.close()