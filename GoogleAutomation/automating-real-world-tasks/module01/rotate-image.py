from PIL import Image
img = Image.open("compass.png")
img.rotate(45).show()
