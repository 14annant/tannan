import os
import qrcode

img = qrcode.make("https://www.linkedin.com/in/tom-a-751046152/")

img.save("qr.png", "PNG")

os.system("open qr.png")