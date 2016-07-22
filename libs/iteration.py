from PIL import Image,ImageEnhance,ImageFilter

def iterate(im, iteration):
    if iteration == 0:
        return im

    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')

    return iterate(im, iteration-1)
