# Pixel Color Cipher (PCC) Python Implementation

from PIL import Image
import math

#Encodes string to pixel image.
def encode_text(text, path):
    HEXD = text.encode(encoding="utf_8").hex() #Converts text to utf 8 hex format
    LGTH = 1
    HIGT = 1
    TARR = [HEXD[i:i+32].ljust(32, "0") for i in range(0, len(HEXD), 32)]

    #Calculate image width
    if(len(str(HEXD)) < 32):
        LGTH = math.ceil(len(str(HEXD))/6)
        HIGT = 1
    elif(len(str(HEXD)) >= 32):
        LGTH = 32
        HIGT = math.ceil(len(TARR)/6)

    HEXT = [HEXD[i:i+6].ljust(6, "0") for i in range(0, len(HEXD), 6)] #Creates array of hex data in 6-character color format

    OIMG = Image.new("RGB", (LGTH,HIGT))

    PIXL = []

    for i, v in enumerate(HEXT):
        CVAL = HEXT[i]
        RGBV = tuple(int(CVAL[i:i+2], 16) for i in (0, 2, 4)) #Converts hex color value to RGB
        PIXL.append(RGBV)
    
    OIMG.putdata(PIXL)
    OIMG.save(path+HEXT[0]+".png")

    print("File '"+HEXT[0]+".png' saved!")

#Encodes hex value to pixel image.
def encode_hex(data, path):
    LGTH = 1
    HIGT = 1
    TARR = [data[i:i+32].ljust(32, "0") for i in range(0, len(data), 32)]

    #Calculate image width
    if(len(str(data)) < 32):
        LGTH = math.ceil(len(str(data))/6)
        HIGT = 1
    elif(len(str(data)) >= 32):
        LGTH = 32
        HIGT = math.ceil(len(TARR)/4)

    HEXT = [data[i:i+6].ljust(6, "0") for i in range(0, len(data), 6)]

    OIMG = Image.new("RGB", (LGTH,HIGT))

    PIXL = []

    for i, v in enumerate(HEXT):
        CVAL = HEXT[i]
        RGBV = tuple(int(CVAL[i:i+2], 16) for i in (0, 2, 4))
        PIXL.append(RGBV)
    
    OIMG.putdata(PIXL)
    OIMG.save(path+HEXT[0]+".png")

    print("File '"+HEXT[0]+".png' saved!")

#Decodes image to hex value.
def decode_file(file):
    FIMG = Image.open(file)
    FDAT = list(FIMG.convert('RGB').getdata())
    HDAT = ""

    for r, g, b in FDAT:
       HDAT += '{:02x}{:02x}{:02x}'.format(r, g, b) #Converts RGB color values to HEX
    
    print(FDAT[0][0])
    print("Decoded hex output: "+HDAT)
    return HDAT

#Converts decoded output to UTF-8 text.
def convert_hex(hex):
    CONV = hex.replace(" ","") #Removes space delimiters
    OUTP = bytes.fromhex(CONV).decode('utf-8') #Converts hex to UTF-8 string

    print("Converted output: "+OUTP)
    return OUTP