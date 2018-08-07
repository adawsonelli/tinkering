"""
pole and record the availibility of spots in the engineering garage over time
"""
#------------------------------ imports ----------------------------------------
import urllib2
import h5py


#------------------------------ polling ----------------------------------------
response = urllib2.urlopen('http://map.wisc.edu/api/v1/map_objects/596/parking_available')
html = response.read()
