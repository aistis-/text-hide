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
  	if counter < len(text_in_binary):
	    R,G,B = pixels[x,y]

	    R_in_bin = list(bin(R))
	    R_in_bin[7] = text_in_binary[counter]

	    R = int("".join(R_in_bin), 2)

	    pixels[x,y] = R,G,B

	    counter += 1

	    

im.save(fnOutput)
print("Completed")
