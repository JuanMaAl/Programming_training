from PIL import Image
img = Image.open("compass.png")
img.rotate(180).resize((1200,1200)).save("flipped_and_resized_compass.png")
