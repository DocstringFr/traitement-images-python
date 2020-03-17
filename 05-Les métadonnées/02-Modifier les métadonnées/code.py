from PIL import Image
import piexif
from pprint import pprint

im_path = "../../_images/rose.jpg"
im = Image.open(im_path)
exif_dict = piexif.load(im_path)
exif_dict['0th'][272] = "Canon 5D"
exif_bytes = piexif.dump(exif_dict)
im.save("../../_images/rose-2.jpg", exif=exif_bytes)
