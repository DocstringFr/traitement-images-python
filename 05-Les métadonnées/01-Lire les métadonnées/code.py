from PIL import Image
import piexif
from pprint import pprint
from PIL import ExifTags

im = Image.open("../../_images/rose.jpg")

exif_dict = piexif.load(im.info["exif"])
pprint(exif_dict)
pprint(ExifTags.TAGS)
