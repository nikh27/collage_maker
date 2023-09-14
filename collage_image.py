from PIL import Image
import numpy as np


def collage_maker(image1,image2,image3,name):
    image_1 = Image.open(image1)
    image_2 = Image.open(image2)
    image_3 = Image.open(image3)

    min_width = min(image_1.width,image_2.width,image_3.width)
    min_height = min(image_1.height,image_2.height,image_3.height)
        
    image_1 = image_1.resize((min_width,min_height))
    image_2 = image_2.resize((min_width,min_height))
    image_3 = image_3.resize((min_width,min_height))

    i1 = np.array(image_1)
    i2 = np.array(image_2)
    i3 = np.array(image_3)

    collage = np.hstack([i1,i2,i3])
    image = Image.fromarray(collage)
    image.save(name)


collage_maker('python/image1.jpg','python/image2.jpg','python/image3.jpg','python/new.jpg')
