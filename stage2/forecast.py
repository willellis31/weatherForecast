#!/usr/bin/python


import httplib		# so we can make a call to the service
import json			# so we can decode the response

#-------------------
def getForecast(latitude, longitude, time):

	url = "api.forecast.io"
	apiKey = '8fc9edcb289fe71e8dea71b64e5caa8b'
	connection = httplib.HTTPSConnection(url)
	path = "/forecast/" + apiKey + "/" + str(latitude) + "," + str(longitude) + "," + str(time) + "T00:00:00"

	connection.request("GET", path)

	response = connection.getresponse()

	# did we get a correct response? (e.g. 200?)
	# should do something if it isn't...

	data = response.read()

	return json.loads(data) # string version
