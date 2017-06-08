#!/usr/bin/env python
import re
import sys
import user_input
import cities
import forecast

def main():
    # Ensure that the user has entered 4 or 5 arguments on the command line
    if (len(sys.argv) < 4):
        print "Error, more values needed at run time"
        print "Please enter a latitude & longitude value, a min population, a date and a time(opt)"
        return
    # assign command line values to variables
    latitude = sys.argv[1]
    longitude = sys.argv[2]
    population = sys.argv[3]
    date_specifier = sys.argv[4]
    time = "00:00:00"
    # assign the time value if it has been entered
    if (len(sys.argv) == 6):
        end_value = sys.argv[(len(sys.argv)-1)]
        time = user_input.processTime(end_value)
    # process input and return values to pass onto weather forecast function
    origin_lat = user_input.verify_latitude(latitude)
    origin_long = user_input.verify_longitude(longitude)
    pop = user_input.verify_population(population)
    date = str(user_input.date_process(date_specifier)) + 'T'
    # get an array of cities
    city_list = cities.getCities()
    # Check that date is correct
    if (date == False):
        print "Error: The date needs to be in YYYY-MM-DD format or a day of the week"
        sys.exit(0);
    # add any extra time to the date specified
    date += time
    # get the nearest city based on population, long and lat values entered
    nearest_city = cities.nearestCity(city_list, pop, origin_long, origin_lat)
    # the lat and long value for the nearest city
    near_city_lat = float(nearest_city[5])
    near_city_long = float(nearest_city[6])
    print "The nearest city is %s" %(str(nearest_city[2]))
    # get the weather forecast
    city_forecast = forecast.getForecast(near_city_lat, near_city_long, date)
    # print the results
    for i in city_forecast['currently']:
            print i + " : " + str(city_forecast['currently'][i])

main()
