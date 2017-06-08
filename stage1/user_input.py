#!/usr/bin/env python
import re
import sys
import datetime
import time
import calendar

def verify_latitude(latitude):
    '''Function to verify and return the latitude value entered in on the commmand line'''
    # regex the input
    result = re.search("(\d*)(N|S)", latitude)
    # try to process entered value and return
    try:
        if (result != None):
            lat = int(result.group(1))
            if (lat < 0 or lat > 90):
                print "Error, latitude value entered needs to be between 0 and 90"
                return False
            elif (result.group(2) == 'N'):
                return lat
            else:
                lat = -lat
                return lat
        else:
            print "Error,latitude value needs to be between 0 and 90 followed by N or S"
            sys.exit(0)
    #catch exception if incorrect value entered
    except ValueError:
        print "Error: latitude needs to be a number followed by a N or S. You entered: ", latitude
        sys.exit(0)



def verify_longitude(longitude):
    '''Function to verify and return the longitude value entered in on the commmand line'''
    # regex the input
    result = re.search("(\d*)(W|E)", longitude)
    # try to process entered value and return if correct
    try:
        if (result != None):
            lon = int(result.group(1))
            if (lon < 0 or lon > 180 ):
                print "Error, longitude value entered needs to be between 0 and 180"
                sys.exit(0)
            elif (result.group(2) == 'E'):
                return lon
            else:
                lon = -lon
                return lon
        else:
            print "Error,longitude value needs to be between -90 and 90 followed by W or E"
            sys.exit(0)
    #catch exception if incorrect value entered
    except ValueError:
        print "Error: Longitude needs to be a number followed by a E or W. You entered: ", longitude
        sys.exit(0)

def verify_population(population):
    '''Function to verify and return the population value entered in on the commmand line'''
    # try to process entered value and return
    try:
        pop = int(population)
        if(pop <= 0):
            print "Population needs to be a whole number greater than zero"
            sys.exit(0)
        return pop
    # catch exception if incorrect value entered
    except ValueError:
        print "Population needs to be a whole number. You entered: ", population
        sys.exit(0)

def date_process(date):
    '''Function to verify and return the date value entered in on the
        commmand line as a timestamp/epoch value'''
    # regex the input
    result = re.search("(now|Now|NOW|today|Today|TODAY)", date)
    # if regex matches return a timestamp for now
    if (result != None):
        today = datetime.date.today()
        return str(today)
    # else see if the user has entered a date in format 2017-MM-DD
    else:
        result = re.search("(2017)\-([0-1]{1}[0-9]{1})\-([0-2]{1}[0-9]{1}|[3]{1}[0-1]{1})", date)
        if (result != None):
            # check date entered is valid
            try:
                valid_date = datetime.date(int(result.group(1)),int(result.group(2)), int(result.group(3)))
                # return entered date as a string
                return str(date)
            # catch exception for invalid date
            except ValueError:
                print "Error in the date value entered. Please check and try again"
                sys.exit(0)
        else:
            # pass user input on to see if they entered a day of the week
            input_date_timestamp = day_process(date);
            return input_date_timestamp

def day_process(day):
    '''Function to check and process the vlaue entered in on the command line
        if the user entered a day of the week. It returns the value of that day
        entered as an epoch value assuming the weekeday is the next occurance of
        that day'''
    # if/else to check the regex for entered weekeday. It sets a value called
    # day_index which will be used to calculate how much time in seconds needs
    # added on to todays timestamp
    result = re.search("(Sunday|Sun|sunday|sun)", day)
    if (result != None):
        day_index = 0
    else:
        result = re.search("(Monday|Mon|monday|mon)", day)
        if (result != None):
            day_index = 1
        else:
            result = re.search("(Tuesday|Tues|tuesday|tues)", day)
            if (result != None):
                day_index = 2
            else:
                result = re.search("(Wednesday|Wed|wednesday|wed)", day)
                if (result != None):
                    day_index = 3
                else:
                    result = re.search("(Thursday|Thurs|thursday|thurs)", day)
                    if (result != None):
                        day_index = 4
                    else:
                        result = re.search("(Friday|Fri|friday|fri)", day)
                        if (result != None):
                            day_index = 5
                        else:
                            result = re.search("(Saturday|Sat|saturday|sat)", day)
                            if (result != None):
                                day_index = 6
                            else:
                                # False returned if a day has not been entered
                                return False
    # get a the date for today
    today = datetime.date.today()
    # get the day of the week as an number Sun = 0, Sat = 6
    today_index = today.strftime("%w")
    # get the days difference between today and the entered weekday
    days_difference = day_index - int(today_index)
    # if days_difference is negative, add 7 to take it to the following
    # week and do the recalculation
    if (days_difference < 0):
        day_index = day_index + 7
        days_difference = day_index - int(today_index)
    # add the correct days onto todays date
    end_date = today + datetime.timedelta(days = days_difference)
    # return the string value of today
    return str(end_date)

def processTime(time):
    '''Function to verify and return the time entered in on the
    commmand line in seconds'''
    hours = 0
    minutes = 0
    # verify input
    result = re.search("(1[0-2]|[0-9]{1})(:?)([0-5]\d{1})?(am|pm)", time)
    if (result != None):
        # check to see if it is a pm time
        if (result.group(4) == 'pm'):
            # add 12 to the hours inputted and concatenate the string
            hours = int(result.group(1)) + 12
            string_time = str(hours) + ":"
        else:
            # start to build up the time string
            string_time = result.group(1) + ":"
        if (result.group(3) != None):
            # add the minutes to the time string if entered
            string_time += result.group(3) + ":00"
        # add value to represent seconds and milliseconds if not entered
        else:
            string_time += "00:00"
        # return the string_time
        return string_time
    else:
        # ensure time is not the 24 hr clock
        print "Error: Time entered can not be 24hr clock. It can be either HH:MM or HH with am or pm at the end"
        sys.exit(0)
