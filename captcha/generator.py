from captcha.image import ImageCaptcha
import string
import random


#generate captcha text
ct = "".join( [random.choice(string.digits + string.ascii_letters) for i in range(6)])

image = ImageCaptcha(width = 280, height = 90)

image.write(ct, 'CAPTCHA.png')