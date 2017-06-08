#!/usr/bin/env python
import re
import sys
import datetime
import time
import calendar


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
                                # get a the date for today
                                today = datetime.date.today()
                                return today
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
