# pip install pillow #
from PIL import Image

# Upload original image #
img = Image.open('img.jpeg')

# Save new compressed image #
img.save(
    'img_compressed.jpg',
    'JPEG',
    optimize=True,
    quality=10
)
