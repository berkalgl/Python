from PIL import Image, ImageFilter

# we have converted or opened up this JPEG
# into an image object that Pillow gives us that we can now manipulate
img = Image.open('./pokedex/pikachu.jpg')

print(img)

# we can access the attributes
print(img.format)
print(img.size)
print(img.mode)

# see the all attributes and methods
print(dir(img))

#-------- Filter ---------

# Let's blur the image
blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save("./pokedex/blurred_pikachu.png", 'png')

# Let's smooth the image
smooth_image = img.filter(ImageFilter.SMOOTH)
smooth_image.save("./pokedex/smooth_pikachu.png", 'png')

# Let's sharpen the image
sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save("./pokedex/sharpen_pikachu.png", 'png')

# we save as a png because png supports these image filters

#-------- Convertion ---------
# L is grayscale
converted_image = img.convert('L')
converted_image.save("./pokedex/grey_pikachu.png", "png")

#-------- Show ---------
# this displays the image
#converted_image.show()

#-------- Rotation --------
crooked = converted_image.rotate(90)
crooked.save("./pokedex/grey_rotated_pikachu.png", "png")

#-------- Resize --------
resize = converted_image.resize((300, 300))
resize.save("./pokedex/resized_pikachu.png", "png")

#-------- Crop --------
box = (100, 100, 400, 400)
region = converted_image.crop(box)
region.save("./pokedex/cropped_grey_pikachu.png", "png")


#-------- Example --------
# Bring down the size of the image by resizing it.

astro_image = Image.open("./astro/astro.jpg")
resized_image = astro_image.resize((400, 400))
resized_image.save("./astro/resized_astro.jpg")

# because the image did not have the same width
# it is actually a little bit compressed and it lost its aspect ratio
# the image looks squished in 

# lets fix it

img.thumbnail((400, 400))
img.save("thumbnail.jpg")