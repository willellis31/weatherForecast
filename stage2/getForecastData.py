#!/usr/bin/python


import httplib		# so we can make a call to the service
import json			# so we can decode the response

#-------------------
def getForecast(url, apikey, latitude, longitude, options):
	connection = httplib.HTTPSConnection(url)
	path = "/forecast/" + apikey + "/" + latitude + "," + longitude  + options
	
	connection.request("GET", path)

	response = connection.getresponse()
	
	# did we get a correct response? (e.g. 200?)
	# should do something if it isn't...
	print response.status
	
	data = response.read()
	
	return json.loads(data) # string version


#-------------------
def main():

	elthamLat = "-37.71528"
	elthamLong = "145.15056"

	# you can insert your api key here
	apiKey = 'your api key'
	
	# or place it in a file...
	file = open(".env")
	apiKey = file.readline().strip()

	
	url = "api.forecast.io"
	#url = "localhost:8000"

	
	forecast = getForecast(url, apiKey, elthamLat, elthamLong)
	
	print forecast
	
main()
