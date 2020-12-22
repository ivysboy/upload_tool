from PIL import Image
from os import listdir
import os
import time
from io import BytesIO


def pinjie():
    # time.sleep(10)
    im_list = [Image.open(os.path.join('./media/upload/', fn)) for fn in listdir('./media/upload') if fn.endswith('.png')]
    ims = []
    for f in im_list:
        print(f.size)
        new_image = f.resize((1280, 1280), Image.BILINEAR)
        ims.append(new_image)
    if len(ims) < 1:
        return
    width, height = ims[0].size
    result = Image.new(ims[0].mode, (width * len(ims), height))
    for i, im in enumerate(ims):
        result.paste(im, box=(i*width, 0))
    result.save('./media/upload/a.png')
    stream = BytesIO()
    result.save(stream, 'png')
    return stream


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pinjie()
