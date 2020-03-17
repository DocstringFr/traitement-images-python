import piexif
from glob import glob
import requests
import shutil
import os

dossier_gps = "../../_images/gps"
dossier_gps_origine = "../../_images/gps/origine"
images = glob(f"{dossier_gps}/*.jpg")

if not os.path.isdir(dossier_gps_origine):
    os.makedirs(dossier_gps_origine)

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
    dossier_pays = os.path.join(dossier_gps, pays)
    if not os.path.isdir(dossier_pays):
        os.makedirs(dossier_pays)

    shutil.copy(image, dossier_pays)
    shutil.move(image, dossier_gps_origine)
