import os
import argparse
from PIL import Image, ImageEnhance

# characters = ".,-~:;=*!#$@"

def value_to_ascii(value, characters):
    # this takes a character's average value and returns an ASCII character. 

    for idx, char in enumerate(characters):
        if value < 255 / len(characters) * idx:
            return f" {char}"
    return "  "

def ascii_convert(input_path, resize_x, resize_y, contrast_factor, flipped):
    img = Image.open(input_path)
    img = img.resize((resize_x, resize_y))
    img = img.convert('RGB')

    # adjust contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(float(contrast_factor))

    output = "\n"
    
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x, y)) # get pixel values in (r, g, b) shape
            average = (pixel[0] + pixel[1] + pixel[2]) / 3
            if flipped:
                output += value_to_ascii(average, "@$#!*=;:~-,.")
            else:
                output += value_to_ascii(average, ".,-~:;=*!#$@")
        output += '\n'

    output = output.split("\n")
    clean_output = output

    for idx, line in enumerate(output):
        for ch in reversed(line):
            if ch == " ":
                clean_output[idx] = clean_output[idx].removesuffix(" ")
            else:
                break

    string_output = ""
    for line in clean_output:
        string_output += line + "\n"

    return string_output

def write_to_file(text, input_path):
    # create output path if it doesn't exist yet
    if not os.path.exists('output/'):
        os.makedirs('output/')

    # gets name of file without the folder its in or its extension
    filename = input_path.split('/')[-1].split('.')[0]

    # create new file (or open it if it's already there), 
    # and write the output to it (it does not wipe previous output, you can compare them that way)
    output_file = open("output/{}.txt".format(filename), 'a')
    # output_file.write(f"Size: {resize_x}, {resize_y} - Contrast: {contrast_factor}")
    output_file.write(text)
    output_file.close()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=str, required=True, help="The input file's location, eg. 'images/logo.png'")
    parser.add_argument('-x', '--resize_x', type=int, required=True, help="The new size of the x-axis")
    parser.add_argument('-y', '--resize_y', type=int, required=True, help="The new size of the y-axis")
    parser.add_argument('-c', '--contrast', type=float, required=False, default=1, help="Factor of how much the contrast should change, >1 = increase, <1 = decrease")
    parser.add_argument('-f', '--flipped', action="store_true", default=False, help="whether or not you want to flip/invert the color")

    args = parser.parse_args()
    text = ascii_convert(args.input, args.resize_x, args.resize_y, args.contrast, args.flipped)
    write_to_file(text, args.input)

if __name__ == "__main__":
    main()