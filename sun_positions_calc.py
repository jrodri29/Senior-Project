#!/usr/bin/python3

import os               											
import urllib.request
import xml	
import xml.etree.ElementTree as ET									
import datetime	
import time
import math

#constants that will not change throughout the calculation
pi = 3.14159265358979323846;
twopi = 2*pi;
rad = pi/180;
dEarthMeanRadius = 6371.01
dAstronmicalUnit = 149597890
dLongitude = -121.31190
dLatitude =37.97580

#get timestamp and make it human readable
timeStamp= time.time()
print (timeStamp)

humanReadable_TS= datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d-%H-%M-%S');
print (humanReadable_TS)

# parse human readable timestamp to create variables for year, month, day, etc.
h = humanReadable_TS.split("-")
print(h)

Year = float(h[0]);
Month = float(h[1]);
Day = float(h[2]);
Hours = float(h[3]);
Minutes = float(h[4]);
Seconds = float(h[5]);

## --Calculating difference between current Julian Day and JD 2451545.0--

#Time of day in UT decimal hours
dDecHours = float(Hours + (Minutes + (Seconds /60.0))/60.0)

#Calculating current Julian Day
liAux1= (Month-14)/12;
liAux2 = (1461*(Year +4800+liAux1))/4 +(367*(Month-2-(12*liAux1)))/12 - (3*((Year +4900+liAux1)/100))/4 + (Day-32075);
print(liAux2)
JDate = float(liAux2) -0.5 +(DecHours)/24.0
#Calculating difference between current Julian Day and JD
ElapJulianDays = JDate -2451545.0
print(ElapJulianDays)
