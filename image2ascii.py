import sys

from PIL import Image
from PIL import ImageOps

def ascii(pmatrix, height, width):

    for y in range(height):
        sentence = ""
        
        for x in range(width):
            gray = pmatrix.getpixel((x,y))

            character = " "
            if gray > 250:
                character = "@"
            elif gray > 230:
                character = "$"
            elif gray > 210:
                character = "&"
            elif gray > 190:
                character = "¥"
            elif gray > 170:
                character = "*"
            elif gray > 150:
                character = "+"
            elif gray > 130:
                character = "/"
            elif gray > 110:
                character = "|"
            elif gray > 90:
                character = ":"
            elif gray > 70:
                character = "."
            elif gray > 50:
                character = " "

            sentence += character
        
        print(sentence)


if __name__ == '__main__':

    try:
        if sys.argv[1] is not None:
          filename = sys.argv[1]
        else:
          raise Exception

        image = Image.open(filename)
        resized_image = image.resize((image.width // 4, image.height // 4))        
        gray_image = ImageOps.grayscale(resized_image)
        width, height = gray_image.size

        ascii(gray_image, height-1 , width-1)

    except Exception as e:
        print(type(e))
        print(e)
