import tkinter
import math
import ssl
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json



GOOGLEAPIKEY = "AIzaSyDIAHoeKUci0TwXf9CeUDYlPW5nr9pdtOc"

class Globals:
   rootWindow = None
   mapLabel = None
   button1 = None
   defaultLocation = "Mauna Kea, Hawaii"
   mapLocation = defaultLocation
   mapFileName = 'googlemap.gif'
   mapSize = 400
   zoomLevel = 9
   maptype = "roadmap"


def increaseBy1():
   Globals.zoomLevel += 1
   updateZoomLevel()
   displayMap()
   
def decreaseBy1():
   Globals.zoomLevel -= 1
   updateZoomLevel()
   displayMap()
   
def updateZoomLevel():
   countLabel.configure(text = "Zoom: {}".format(Globals.zoomLevel))

def maptype():
   global choicetype
   if choicetype.get() == 1:
      Globals.maptype = "roadmap"
      displayMap()
   elif choicetype.get() == 2:
      Globals.maptype = "terrain"
      displayMap()
   elif choicetype.get() == 3:
      Globals.maptype = "hybrid"
      displayMap()
   else:
      Globals.maptype = "satellite"
      displayMap()
   Label2.configure(text = "Map view choice is: {}".format(Globals.maptype))
   
   



def geocodeAddress(addressString):
   global geoURL
   global jsonResult
   urlbase = "https://maps.googleapis.com/maps/api/geocode/json?address="
   geoURL = urlbase + quote_plus(addressString)
   geoURL = geoURL + "&key=" + GOOGLEAPIKEY

   
   ctx = ssl.create_default_context()
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   
   stringResultFromGoogle = urlopen(geoURL, context=ctx).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      result = (0.0, 0.0)    
   else:
      loc = jsonResult['results'][0]['geometry']['location']
      result = (float(loc['lat']),float(loc['lng']))
   return result

def getMapUrl(lat, lng):
   lat, lng = geocodeAddress(Globals.mapLocation)
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   args = "center={},{}&zoom={}&size={}x{}&maptype={}&format=gif&markers=color:red|label|{},{}".format(lat,lng,Globals.zoomLevel,Globals.mapSize,Globals.mapSize,Globals.maptype,lat,lng)
   args = args + "&key=" + GOOGLEAPIKEY
   mapURL = urlbase + args
   return mapURL

def retrieveMapFromGoogle():
   lat, lng = geocodeAddress(Globals.mapLocation)
   url = getMapUrl(lat, lng)
   urlretrieve(url, Globals.mapFileName)
   
def displayMap():
   retrieveMapFromGoogle()    
   mapImage = tkinter.PhotoImage(file=Globals.mapFileName)
   Globals.mapLabel.configure(image=mapImage)
   
   Globals.mapLabel.mapImage = mapImage
   
def readEntryAndDisplayMap():
   global Entry
   
   Globals.mapLocation = Entry.get()
   displayMap()


def initializeGUIetc():
   global Entry 
   global button1
   global Label1
   global countLabel
   global Label2
   global mapType
   global rootWindow
   global choicetype
   

   
   Globals.rootWindow = tkinter.Tk()
   Globals.rootWindow.title("HW9")
   Globals.locationEntry = tkinter


   mainFrame = tkinter.Frame(Globals.rootWindow) 
   mainFrame.pack()


      
   choicetype = tkinter.IntVar()
   choicetype.set(1)
   
   
   topFrame = tkinter.Frame(mainFrame)
   topFrame.pack()
   bottomFrame = tkinter.Frame(mainFrame)
   bottomFrame.pack()
   increaseButton = tkinter.Button(topFrame, text = '+', command = increaseBy1)
   increaseButton.pack(side = tkinter.LEFT)
   decreaseButton = tkinter.Button(topFrame, text = '-', command= decreaseBy1)
   decreaseButton.pack(side = tkinter.LEFT)
   countLabel = tkinter.Label(topFrame, text= "zoom: {}".format(Globals.zoomLevel))
   countLabel.pack(side = tkinter.LEFT)
   Label1 = tkinter.Label(topFrame, text  = "Enter Location here")
   Label1.pack(side = tkinter.RIGHT)
   choice1 = tkinter.Radiobutton(Globals.rootWindow, text = "roadmap", variable = choicetype, value = 1, command  = maptype)
   choice1.pack()
   choice2 = tkinter.Radiobutton(Globals.rootWindow, text = "terrain", variable = choicetype, value = 2, command = maptype)
   choice2.pack()
   choice3 = tkinter.Radiobutton(Globals.rootWindow, text = "hybrid" , variable = choicetype, value = 3, command = maptype)
   choice3.pack()
   choice4 = tkinter.Radiobutton(Globals.rootWindow, text = "satellite", variable = choicetype, value = 4, command = maptype)
   choice4.pack()
   Label2 = tkinter.Label(Globals.rootWindow, text = "Map view choice is: {}".format(Globals.maptype))
   Label2.pack()
   Entry = tkinter.Entry(topFrame)
   Entry.pack(side = tkinter.LEFT)

   
   readEntryAndDisplayMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndDisplayMap)
   readEntryAndDisplayMapButton.pack()

   
   
   
   Globals.mapLabel = tkinter.Label(mainFrame, width=Globals.mapSize, bd=2, relief=tkinter.FLAT)
   Globals.mapLabel.pack()

def HW9():
    global Entry
    global button1
    global maptype
    initializeGUIetc()
    displayMap()
    Globals.rootWindow.mainloop()

