from PIL import Image

img = Image.open('house.png').convert('LA')
img.save('greyscale.png')
