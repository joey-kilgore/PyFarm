# Test script that will use Pillow to generate photos


from PIL import Image
import random
import numpy as numpy
#import PyFarm
import base64
from io import BytesIO

numberOfImages = 1#PyFarm.input(0)

#arr = numpy.random.randint(0,255,(100,100,3),dtype='uint8') #Pillow interprets type as uint8, not int32
#print(arr)
#im = Image.fromarray(arr, 'RGB')
#im.show()

for num in range(0,numberOfImages):
    im = Image.new('RGBA',(100,100))
    pixels = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
    im.show()

buffered = BytesIO()
im.save(buffered, format="PNG")
imb64 = base64.b64encode(buffered.getvalue())

print(imb64)
#PyFarm.output(imb64)

#im = Image.new('RGB',(100,100))
#pixels = im.load()
#for x in range(im.size[0]):
#	for y in range(im.size[1]):
#		pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#im.show()

