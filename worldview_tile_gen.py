#!/usr/bin/python

import os

#Worldview downloader Degree footprint values allowed based on 8200x8200 image max size

#res = '5km'
#deg = 90

res = '1km'
deg = 60

#res = '500m'
#deg = 30


#Calculate number of tiles per row and column
row = int(180/deg)
col = int(360/deg)

#lower left corner at which to start
west = -180
south = -90

mac_chrome_cmd = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome '

for i in range(col):
	xmin=west+deg*(i)
	xmax=xmin+deg
	for j in range(row):
		print 
		ymin=south+deg*(j)
		ymax=ymin+deg
		footprint = ymin,xmin,ymax,xmax
		cmd = mac_chrome_cmd + '"https://wvs.earthdata.nasa.gov/?LAYERS=VIIRS_SNPP_CorrectedReflectance_TrueColor&CRS=EPSG:4326&TIME=2016-11-25&COORDINATES='+str(ymin)+','+str(xmin)+','+str(ymax)+','+str(xmax)+'&FORMAT=image/tiff&AUTOSCALE=FALSE&RESOLUTION='+res+'"'
		print (cmd)
		os.system(cmd)
