from PIL import Image

img = Image.open("dukelogo.png")
img.show()
pixels = [(0,b,g) for (r,g,b) in img.getdata()]
img.putdata(pixels)
img.show()
