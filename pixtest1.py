from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)


#font = ImageFont.truetype("examples/pixelmix.ttf", 8)

#with canvas(device) as draw:
#    draw.rectangle(device.bounding_box, outline="white", fill="black")
   
#sleep(2)

import random
from PIL import Image
image = Image.new('1', (8, 8))

while True:
	x = random.randint(0,7)
	y = random.randint(0,7)
	image.putpixel((x, y), 1)
	device.display(image)
	sleep(.05)
	image.putpixel((x, y), 0)
        device.display(image)
      

