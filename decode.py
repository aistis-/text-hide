#!/usr/bin/python

import Image, binascii

fnInput ="picture_out1.png"

im = Image.open(fnInput)
print "Opened ", im.format, im.size, im.mode
pixels = im.load()

text_in_binary = []
text = []

for y in xrange(im.size[1]):
    for x in xrange(im.size[0]):
        R,G,B = pixels[x,y]

        try:
            binary = bin(R)
            text_in_binary.append(binary[7 + 2])
            binary = bin(G)
            text_in_binary.append(binary[7 + 2])
            binary = bin(B)
            text_in_binary.append(binary[7 + 2])
        except IndexError:
            break;


for counter in range(len(text_in_binary) - 1):
    char_in_bin = ['0', 'b']

    for i in range(8):
        try:
            char_in_bin.append(text_in_binary[counter])
        except IndexError:
            break

        counter += 1

    string = "".join(char_in_bin)

    text.append(chr(int(string, 2)))

print("".join(text))
