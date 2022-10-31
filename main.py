# %%
from PIL import Image
from PIL.ImageEnhance import Brightness


img_path = "img.jpg"

# TODO load in images with PIL
img = Image.open(img_path)
print(img)
img.show()
# img.save() # TODO convert to PNG
# img = img.convert("L")  # TODO convert to grayscale
# print(img)
# img.show()


# TODO apply filters
brightness_enhancer = Brightness(image=img)
print(brightness_enhancer)

img = brightness_enhancer.enhance(0.5)
img.show()

# but what is a filter?

# TODO apply a uniform filter to blur
# TODO apply a gaussian filter to denoise
# TODO resize
# TODO create pipeline of these transformations
# TODO normalise
# TODO create processed image generator

# %%
img = Image.open("img.jpg")
img.show()
# %%
