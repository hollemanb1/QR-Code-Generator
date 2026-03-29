# User Intrface for Nayuki QR-Code Generator
# Brody Holleman - 3/28/26
# Nayuki Copyright Info Below

# QR Code generator library (Python)
# 
# Copyright (c) Project Nayuki. (MIT License)
# https://www.nayuki.io/page/qr-code-generator-library
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# - The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
# - The Software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and noninfringement. In no event shall the
#   authors or copyright holders be liable for any claim, damages or other
#   liability, whether in an action of contract, tort or otherwise, arising from,
#   out of or in connection with the Software or the use or other dealings in the
#   Software.

from Nayuki.qrcodegen import QrCode
# from qrcodegen import QrCode
from PIL import Image
import os

print("Input URL: ", end = " ")
url = input()

print("Input QR Filename (No Extension - invalid characters will be replaced with '_'): ", end = " ")
filename = input()

qr = QrCode.encode_text(url, QrCode.Ecc.LOW)

size = qr.get_size()
scale = 10
img = Image.new("RGB", (size * scale, size * scale), "white")

for y in range(size):
    for x in range(size):
        if qr.get_module(x, y):
            for dy in range(scale):
                for dx in range(scale):
                    img.putpixel((x*scale+dx, y*scale+dy), (0, 0, 0))
                    
chars = list(filename)
                    
for i in range(0, len(chars)):
    # Check for invalid characters for filename
    if ((ord(chars[i]) < 65 or ord(chars[i]) > 90) and # Not Uppercase Letter
        (ord(chars[i]) < 97 or ord(chars[i]) > 122) and # Not Lowercase Letter
        (ord(chars[i]) < 48 or ord(chars[i]) > 57) # Not Number
        and ord(chars[i]) != 45 and ord(chars[i]) != 95): # Not Hyphen/Underscore
        chars[i] = '_'

filename = ''.join(chars)
filename = filename + ".png"

os.makedirs("QR Codes", exist_ok=True)
img.save(os.path.join("QR Codes", filename))

print("QR Code Generated! Goodbye!")