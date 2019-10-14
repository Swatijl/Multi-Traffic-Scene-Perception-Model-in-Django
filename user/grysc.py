from PIL import Image
img = Image.open('Chrysanthemum.jpg').convert('LA')
img.save('greyscale.png')