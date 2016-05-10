#!/usr/bin/env python3
#
# Weather blocklet script for i3blocks

import os
from pyowm import OWM

# Set the api key before using this script
api_key = "YOUR OPEN_WEATHER_MAP API_KEY"

FA_SUN = "<span font='FontAwesome'>\uf0a3</span>"
FA_MOON = "<span font='FontAwesome'>\uf186</span>"
FA_CLOUD = "<span font='FontAwesome'>\uf0c2</span>"
FA_UMBRELLA = "<span font='FontAwesome'>\uf0e9</span>"
FA_ASTERIKS = "<span font='FontAwesome'>\uf069</span>"
FA_ALIGN_LEFT = "<span font='FontAwesome'>\uf036</span>"
FA_UNLINK = "<span font='FontAwesome'>\uf127</span>"

city_id  = os.environ.get('BLOCK_INSTANCE')
if not city_id:
    # Defaults to London, UK
    city_id = 2643743
try:
    owm = OWM(api_key)
    obs = owm.weather_at_id( int(city_id) )
    w = obs.get_weather()
except Exception:
    # If api call failed, shows error message
    text = FA_UNLINK + " NO CONNECTION"
    print(text)
    print(text)
    exit(33)

text = ""
temp = w.get_temperature('celsius')['temp']
wtype = w.get_weather_icon_name()

if wtype.startswith('01') or wtype.startswith('02'):
    # Clear
    if wtype[2] == 'd':
        text += "<span color='yellow'>{}</span>".format(FA_SUN)
    else:
        text += FA_MOON
elif wtype.startswith('03') or wtype.startswith('04'):
    # Cloudy
    text += FA_CLOUD
elif wtype.startswith('09') or wtype.startswith('10') or wtype.startswith('11'):
    # Rainy
    text += FA_UMBRELLA
elif wtype.startswith('13'):
    # Snowy
    text += FA_ASTERIKS
elif wtype.startswith('50'):
    # Misty
    text += FA_ALIGN_LEFT
else:
    # Unknown
    text += FA_UNLINK

text += str(round(temp)).rjust(3) 
# Degree symbol
text += '\u00b0'

print(text)
print(text)
