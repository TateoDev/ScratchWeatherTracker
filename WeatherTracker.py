from scratch2py import Scratch2Py
import requests
from time import sleep


s2py = Scratch2Py('_tate', *PASSWORD*)

cloudproject = s2py.scratchConnect('574764513')

#Cloud Connection testing
cloudproject.setCloudVar('CloudVar', 12)

while True:
  r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=83709,us&appid=*KEY=imperial")
  r_json = r.json()
  print(r_json["main"]["temp"])
  cloudproject.setCloudVar('temp', r_json["main"]["temp"])
  sleep(60)
