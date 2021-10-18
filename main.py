import sys
import os

clear_console = 'clear' if os.name == 'posix' else 'CLS'

from PIL import Image, ImageEnhance

def txt_to_ascii_flip(average):
    # flipped version of regular conversion function. this takes a character's average value and returns an ASCII character

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
    # this takes a character's average value and returns an ASCII character. 
    # I may need to change this to a cleaner solution, but for now this works fine.

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

# opens given image, asks for new dimensions and resizes to them (so the art isn't too big), and converts to RGB (so getpixel works)
img = Image.open(input_path)

resize_x = int(input("x axis size: "))
resize_y = int(input("y axis size: "))

img = img.resize((resize_x, resize_y))
img = img.convert('RGB')

contrast_factor = input("Would you like to increase contrast? 1 = no chance, >1 = increase, <1 = decrease. ")

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(float(contrast_factor))

# used to determine wether txt_to_ascii() or txt_to_ascii_flip() is used 
flipped = input('do you want to flip the colors (y/n)? ')

# two linebreaks in case there is previous output in the file (since it only writes, it doesnt wipe the previous runs. that way you can compare.)
output = '\n\n'

# iterate over each pixel
for y in range(img.size[1]):
    for x in range(img.size[0]):
        pixel = img.getpixel((x, y)) # get pixel values in (r, g, b) shape
        average = (pixel[0] + pixel[1] + pixel[2]) / 3
        if flipped == 'y':
            output += txt_to_ascii_flip(average)
        else:
            output += txt_to_ascii(average)
    output += '\n'

output = output.split("\n")
clean_output = output

for i_index, i in enumerate(output):
    for ch in reversed(i):
        if ch == " ":
            clean_output[i_index] = clean_output[i_index].removesuffix(" ")
        else:
            break

string_output = ""
for each in clean_output:
    string_output += each + "\n"

# create output path if it doesn't exist yet
if not os.path.exists('output/'):
    os.makedirs('output/')

# gets name of file without the folder its in or its extension
filename = input_path.split('/')[-1].split('.')[0]

# create new file (or open it if it's already there), 
# and write the output to it (it does not wipe previous output, you can compare them that way)
output_file = open("output/{}.txt".format(filename), 'a')
output_file.write(f"Size: {resize_x}, {resize_y} - Contrast: {contrast_factor}")
output_file.write(string_output)
output_file.close()