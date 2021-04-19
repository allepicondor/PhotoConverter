from PIL import Image
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser()
parser.add_argument("image")
args = parser.parse_args()
image = args.image
def add_border(image_path):
    baseheight = 1080

    img = Image.open(image_path, 'r')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)



    img_w, img_h = img.size
    background = Image.new('RGB', (1920, 1080), (255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save(image_path.split(".")[0]+"2"+".jpg")
if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg") or image.endswith(".gif") or image.endswith(".gif"):
    print(image)
    add_border(image)
else:
    onlyfiles = [f for f in listdir(image) if isfile(join(image, f))]
    print(onlyfiles)
    for file in onlyfiles:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".gif"):
            add_border(file)
            print(file)
