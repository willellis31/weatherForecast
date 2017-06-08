#!/usr/bin/python


import httplib
import json
import sys

def getForecast(latitude, longitude, time):
    '''Function to get the forecast for a given city'''
    try:
        # api key and url for site
        url = "api.forecast.io"
        apiKey = '8fc9edcb289fe71e8dea71b64e5caa8b'
        # obtain a connection
        connection = httplib.HTTPSConnection(url)
        # concatenate the rest of the path
        path = "/forecast/" + apiKey + "/" + str(latitude) + "," + str(longitude) + "," + str(time)
        # send request
        connection.request("GET", path)
        # store response
        response = connection.getresponse()
        # read in the response
        data = response.read()
        # return and string JSON
        return json.loads(data) # string version
    # catch a 404 error if received from the website and exit
    except ValueError:
        print "Error: There was a problem retrieving the forecast from the API - check your inputed values"
        sys.exit(0)
