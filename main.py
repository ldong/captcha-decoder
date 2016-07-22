from PIL import Image

from libs import iteration
from libs import convert_to_text

def main():
    im = Image.open('sample.jpeg')
    im = iteration.iterate(im, 2)

    # comment it out to see the actual processed image
    # im.show()

    convert_to_text.get_string_from_image(im)
    text = convert_to_text.get_string_from_image(im)
    print text


if __name__ == "__main__":
    main()
