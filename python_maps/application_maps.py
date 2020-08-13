# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:11:20 2020

@author: user
"""
from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="application_maps")


data = pd.read_html('https://fr.wikipedia.org/wiki/Liste_des_wilayas_d%27Alg%C3%A9rie')
wilaya_info=pd.DataFrame(data[2])
wilaya_info.to_excel('wilayas_localisation.xlsx',header=True)



get_wilaya_info =pd.read_excel('wilayas_localisation.xlsx',usecols=[2],names=['wilaya'],header=None,skiprows=1,nrows=48)


t_latitude=[]
t_longitude= []
for data_info in get_wilaya_info['wilaya']:
    if 'Wilaya de 'or 'Wilaya d' in data_info:
        wilaya=data_info.replace('Wilaya de ','').replace('Wilaya d\'','')
        location = geolocator.geocode(wilaya)
        t_latitude.append(location.latitude)
        t_longitude.append(location.longitude)
        


wilaya_info['latitude']=pd.Series(t_latitude)
wilaya_info['longitude']=pd.Series(t_longitude)
wilaya_info.to_excel('wilayas_localisation.xlsx',header=True)