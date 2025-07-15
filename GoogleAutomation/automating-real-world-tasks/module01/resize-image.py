from PIL import Image
img = Image.open("compass.png")
new_img = img.resize((1200,1200))
new_img.save("bigcompass.png")
