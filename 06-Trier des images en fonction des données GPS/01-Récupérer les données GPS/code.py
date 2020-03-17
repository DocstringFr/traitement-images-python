import piexif
from glob import glob
import requests

dossier_gps = "../../_images/gps"
images = glob(f"{dossier_gps}/*.jpg")

for image in images:
    exif_dict = piexif.load(image)

    try:
        lat = exif_dict.get("GPS").get(piexif.GPSIFD.GPSLatitude)
        lon = exif_dict.get("GPS").get(piexif.GPSIFD.GPSLongitude)
    except IndexError:
        continue

    lat = lat[0][0]
    lon = lon[0][0]

    r = requests.get(f"https://nominatim.openstreetmap.org/reverse.php?format=json&lat={lat}&lon={lon}")
    pays = r.json().get("address").get("country")
