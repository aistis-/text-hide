#!/usr/bin/python

import Image, binascii

# "Remove" least significant bits in the image file

fnInput ="picture.png"
nb=1 # number of least signif. bits to remove 
fnOutput="picture_out%d.png" % nb 

text_to_encode = "Some text 123"
text_in_binary = bin(int(binascii.hexlify(text_to_encode), 16))


im = Image.open(fnInput)
print "Opened ", im.format, im.size, im.mode
pixels = im.load()

counter = 2;

for y in xrange(im.size[1]):
    for x in xrange(im.size[0]):
        R,G,B = pixels[x,y]

        if counter < len(text_in_binary):
            binary = list(bin(R))
            binary[7] = text_in_binary[counter]

            R = int("".join(binary), 2)

            counter += 1

        if counter < len(text_in_binary):
            binary = list(bin(G))
            binary[7] = text_in_binary[counter]

            G = int("".join(binary), 2)

            counter += 1

        if counter < len(text_in_binary):
            binary = list(bin(B))
            binary[7] = text_in_binary[counter]

            B = int("".join(binary), 2)

            counter += 1

        pixels[x,y] = R,G,B





im.save(fnOutput)
print("Completed")
