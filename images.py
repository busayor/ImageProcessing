from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_image = img.filter(ImageFilter.SHARPEN)
filtered_image = img.convert('L')
rotated = filtered_image.rotate(90)
resized = filtered_image.resize((300,300))
resized.save("grey.png", 'png')
# filtered_image.show()


family_img = Image.open('family.jpg')
# print(family_img.size)
family_img.thumbnail((400,200))
family_img.save("thumbnail.jpg")
print(family_img.size)