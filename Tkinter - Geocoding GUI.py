import tkinter
import tkinter.messagebox
from urllib.request import urlopen
from urllib.parse import urlencode
from xml.etree import ElementTree
api_url="http://maps.googleapis.com/maps/api/geocode/xml?"
window=tkinter.Tk()
window.title("Google Maps Geocoding API")
window.geometry('1050x250')
lbl=tkinter.Label(window,text="Enter your address here. ->")
lbl.grid(column=0,row=0)
info=tkinter.Label(window,text="Hi! I\'m GeoTkinter. I am a Graphical-User-Interface Mode of the previous Geocoding program.\nFirst, enter an address, then click on my button to have the coordinate version of your address.\nThanks for using!")
info.grid(column=3,row=1)
pythonsig=tkinter.PhotoImage(file="Python-Powered.png")
pythonlabel=tkinter.Label(window,image=pythonsig)
pythonlabel.grid(column=3,row=2)
txt=tkinter.Entry(window,width=70)
txt.grid(column=3,row=0)
txt.focus()
def geocode():
    try:
        address=txt.get()
        if len(address)<1:
            return
        url=api_url+urlencode({"address":address})
        data=urlopen(url).read()
        tree=ElementTree.fromstring(data)
        res=tree.findall("result")
        lat=res[0].find("geometry").find("location").find("lat").text
        lng=res[0].find("geometry").find("location").find("lng").text
        lat=float(lat)
        lng=float(lng)
        lat_c="S" if lat<0 else "N"
        lng_c="W" if lng<0 else "E"
        location=res[0].find("formatted_address").text
        A="===>"+location+"<===\n"
        B="Latitude: {0:.10f}{1}\n".format(abs(lat),lat_c)
        C="Longitude: {0:.10f}{1}".format(abs(lng),lng_c)
        result=str(A+B+C)
        tkinter.messagebox.showinfo(f"Coordinate for {address}",result)
    except IndexError as err:
        tkinter.messagebox.showerror(f"Failed to retrieve data","I can\'t find {} in Google Maps.\nPlease re-check the address you entered.".format(address))
    except Exception as err:
        tkinter.messagebox.showerror(f"No internet connection","I need internet to get the results you wanted.\nPlease connect to internet for the results.")
button=tkinter.Button(window,text="Show coordinate",command=geocode)
button.grid(column=5,row=0)
window.mainloop()
