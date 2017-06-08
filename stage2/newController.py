#!/usr/bin/python

import cgi
import json
import urllib
import cities
import user_input
import forecast

def createLongLatPage():
	getIpLocation()
	data = "<html><head><title>Demonstration of a webserver</title></head><body>\n"
	data += '<form action="http://127.0.0.1:34567/longlat" method="POST">\n'

	data += '<label for="longitude">Longitude</label>'
	data += '<input type="text" name="longitude"></input>'

	data += '<label for="latitude">Latitude</label>'
	data += '<input type="text" name="latitude"></input>'

	data += '<input type="submit" id="submit"></submit>'
	data += '</form>'
	data += '</body></html>\n'

	return data


def respondToLongLat(parameters):

	return "i am responding to the page"

#--------------------------------
def createWebFormPage():
	cities = processIpInformation()
	data = "<html><head><title>Demonstration of a webserver</title></head><body>\n"
	data += '<form action="http://127.0.0.1:34567/" method="POST">\n'
	data += 'hello there!'
	data += '<input type="text" name="name"></input>'
	data += '<select name="weekday">'
	data += '<option value="Today">Today</option>'
	data += '<option value="Monday">Monday</option>'
	data += '<option value="Tuesday">Tuesday</option>'
	data += '<option value="Wednesday">Wednesday</option>'
	data += '<option value="Thursday">Thursday</option>'
	data += '<option value="Friday">Friday</option>'
	data += '<option value="Saturday">Saturday</option>'
	data += '<option value="Sunday">Sunday</option>'
	data += '</select>'
	data += '<select name="city">'
	for i in range (0,9):
		data += '<option value="' + str(cities[i][2]) + '">' + str(cities[i][2]) + '</option>'
	data += '</select>'
	data += '<input type="submit" id="submit"></submit>'
	data += '</form>'
	data += '<br><a href="https://darksky.net/poweredby/">Powered by DarkSky</a>'
	data += '</body></html>\n'

	return data

#--------------------------------
def respondToSubmit(parameters):
	name = parameters['name']
	location = parameters['city']
	weekday = parameters['weekday']

	data = "<h1>Thanks <b>%s</b>!" % name
	data += "</h2>"
	data += "<br/>The weather at %s on %s is..." %(location, weekday)
	data += "<br/><br/>"
	data += getWeather(location, weekday)
	data += '<br><a href="https://darksky.net/poweredby/">Powered by DarkSky</a>'

	return data

def processIpInformation():

	url = "http://freegeoip.net/json/"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	lon = data['longitude']
	lat = data['latitude']
	city_list = cities.getCities()
	city_array = getClosestCities(city_list, lon, lat)
	return city_array

def getClosestCities(city_list, lon, lat):
	closestCities = []
	maximum_distance = 10000000 #upper band
	for city in city_list:
		if (len(closestCities) < 9):
			closestCities.append(city)
			continue
		for i in range(0,9):
			distance = cities.distanceBetweenCities(float(lon), float(lat), float(city[6]), float(city[5]))
			distance2 = cities.distanceBetweenCities(float(lon), float(lat), float(closestCities[i][6]), float(closestCities[i][5]))
			if (distance2 > distance):
				city2 = closestCities.pop(i)
				closestCities.insert(i, city)
				city = city2
			else:
				continue
	saveClosestCities(closestCities)
	return closestCities

def saveClosestCities(closestCities):
	citiesToSave = []

	for line in closestCities:
		citiesToSave.append(line)
	f = open("closestCitiesList.txt", 'w')
	for line in citiesToSave:
		f.write("%s\n" % line)
	f.close()


def getWeather(city, day):
	location = city
	data = [line.strip() for line in open("closestCitiesList.txt", 'r')]

	cities = [line.split(",") for line in data]
	for city in cities:
		city_name = city[2].split("'")
		if(str(city_name[1]) == location):
			lon = city[6].split("'")
			lat = city[5].split("'")
			lon = lon[1]
			lat = lat[1]
	time = user_input.day_process(day)
	city_forecast = forecast.getForecast(lat, lon, time)
	weather_data =""
	for i in city_forecast['currently']:
		if (i == 200):
			continue
		else:
			weather_data += i + " : " + str(city_forecast['currently'][i]) + "<br/>"
	return weather_data
