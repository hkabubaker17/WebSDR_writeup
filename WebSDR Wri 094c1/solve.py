import math
from xml.etree.ElementTree import PI
from PIL import Image


a = 17
im = Image.open("aa.png")

w, h = im.size
condition = True

binary = ""

for i in range(w):


    if im.getpixel((i, 375))[0] > 200 and condition == True:

        z = 0
        for c in range(i,i+200):
            try:
                if im.getpixel((c, 375))[0] > 200:
                    z += 1
                else:
                    break
            except:
                break

        z = round(z/a)
        condition = False
        binary += "1" * z


    if im.getpixel((i, 375))[0] < 200 and condition == False:
        
        z = 0
        for c in range(i,i+200):
            try:
                if im.getpixel((c, 375))[0] < 200:
                    z += 1
                else:
                    break
            except:
                break

        z = round(z/a)
        condition = True
        binary += "0" * z

flag = ""
for i in range (binary.find("01001000"),len(binary),12):
    c = chr(int(binary[i:i+8],2))
    flag = flag + c
    if c == '}':
        print("Flag :",flag)
        break
