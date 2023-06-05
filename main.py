import os
import pathlib
from PIL import Image

path = r'D:\new_images'
cur = pathlib.Path(path)
end = '.webp'

i = 0
for root, dirs, files in os.walk(path):
    for name in files:
        old = os.path.join(root, name)
        newfile = os.path.join(root, str(name).split('.')[0] + end)
        image = Image.open(old)

        # Convert and save as WebP
        image.save(newfile, "WebP")
        print(i, newfile)
        i+=1
