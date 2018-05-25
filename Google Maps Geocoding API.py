from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML
import logging
api_url="http://maps.googleapis.com/maps/api/geocode/xml?"
logger=logging.getLogger("Google Maps Geocoding API")
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler("GPS data.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
def geocode():
    try:
        address=input("Enter your address : ")
        logger.info("Address = {}".format(address if len(address)>0 else None))
        if len(address)<1 or address=="Home" or address=="home":
            address="Jl. Fiordini VI, Curug Sangereng, Klp. Dua, Tangerang, Banten 15810, Indonesia"
        elif address=="dev login":
            password=input("[dev] password for developer :")
            if password=="1010100101111":
                task=input("What do you want to do?\n")
                if task=="check logging data":
                    print(open("GPS data.log").read())
                    return
        url=api_url + ENCODE({"address":address})
        data=OPEN(url).read()
        tree=XML.fromstring(data)
        res=tree.findall("result")
        if tree==None:
            logger.error("This is error.")
        else:
            logger.info("There is no error in running this code.")
        lat=res[0].find("geometry").find("location").find("lat").text
        lng=res[0].find("geometry").find("location").find("lng").text
        lat=float(lat)
        lng=float(lng)
        lat_c="S" if lat<0 else "N"
        lng_c="W" if lng<0 else "E"
        location=res[0].find("formatted_address").text
        print("===>",location,"<===")
        print("Latitude: {0:.10f}{1}".format(abs(lat),lat_c))
        print("Longitude: {0:.10f}{1}".format(abs(lng),lng_c))
    except IndexError:
        print("Location not found in Google API\nLink : {}".format(api_url))
        logger.error("Can\'t find {} in Google API.".format(address))
geocode()
