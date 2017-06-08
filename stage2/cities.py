#!/usr/bin/env python
import re
import sys
import datetime
import string
import time
import calendar
from math import sin, cos, sqrt, atan2, radians

def distanceBetweenCities(lon1, lat1, lon2, lat2):
# sourced from https://stackoverflow.com/questions/19412462/getting-distance-
# between-two-points-based-on-latitude-longitude
    '''Function to calculate the distance between two points on the globe'''
    # R is the radius of the globe
    R = 6373.0
    # turn long and lat values into radians
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    # calculate the difference between the points
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    # apply the harversine calculation
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # calculate the distance and return
    distance = R * c
    return distance

def nearestCity(cities, population, lon, lat):
    '''Function to calculate the nearest city to the entered long and lat values '''
    closest_city = ''
    # create a distance value to campare to
    maximum_distance = 10000000
    for city in cities:
        # find out if the pop entered is less than the population of a given city
        if (int(city[4]) > population):
            # calculate the distance to the city if the population is greater
            distance = distanceBetweenCities(float(lon), float(lat), float(city[6]), float(city[5]))
            # check the distance is less than the previously stroed value
            if (distance < maximum_distance):
                closest_city = city
                maximum_distance = distance
    # return final value for closest_city
    return closest_city

def getCities():
    '''Function to get the cities to be checked against for main program '''
    # ensure there is only data in each line
    data = [line.strip() for line in open("../stage1/filteredcities.txt", 'r')]
    # split each line into individual sections
    cities = [line.split(",") for line in data]
    # return array
    return cities
