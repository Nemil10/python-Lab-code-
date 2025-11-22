from PIL import Image, ImageOps

img = Image.open(r"C:\Users\Nemilchhagani\OneDrive\Desktop\MU.jpg")
padded = ImageOps.expand(img, border=20, fill='black')
padded.show()