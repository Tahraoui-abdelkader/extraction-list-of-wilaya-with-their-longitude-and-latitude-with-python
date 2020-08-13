# Extraction-list-of-wilaya-with-their-longitude-and-latitude-with-python


Longitude and altitude have a big role in the precision of the position and for the extraction of it will see a method among 
we will see a method that makes it easier for us to find the positions of several addresses with python language.I used the geopy library

##  geopy 

geopy is a Python client for several popular geocoding web services.

geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.


geopy includes geocoder classes for the [OpenStreetMap Nominatim](https://nominatim.org/), [Google Geocoding API (V3)](https://developers.google.com/maps/documentation/geocoding/overview)


## Installation

Install using pip with:

`pip install geopy                                                 `

Or,[download a wheel or source archive from PyPI](https://pypi.org/project/geopy/).

## Geocoding

### Example
```python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="app_name")
location = locator.geocode("Palais De La Culture Moufdi Zakaria")
print(location.address)
>>Palais de la Culture Moufdi Zakaria, Rue Bouder, Jardin aoumar merar, Kouba, Hussein Dey, الجزائر, 16000, الجزائر
print((location.latitude, location.longitude))
>>(36.73803975, 3.082081439998296)
