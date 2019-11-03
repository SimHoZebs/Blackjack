# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:48:12 2019

@author: Zebs

The goal of this program is to output the difference between the date of input and current day.
"""

import time

print ("Input month, date, and year of time (in numbers) you wish to know how far it is from now.")

month = input("Month?:")
date = input("Date?:")
year = input("Year?:")

#Extracing current time information
curr_time = str(time.localtime()).split(',')
curr_month = curr_time[1][8:]
curr_date = curr_time[2][9:]
curr_year = curr_time[0][-4:]

year_diff = curr_year - year
month_diff = curr_month - month
date_diff = curr_date - date
total_diff = 0
days_feb = 0

if curr_year%4==0:
    days_feb = 29
else:
    days_feb = 28

month_list_r = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, days_feb, 31]
month_list = [0, 31, days_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if date_diff > 0:
    total_diff += date_diff
else:
    total_diff += month_list[curr_month] - curr_date
    
    if month_diff > 0:
        
    

total_diff += 365*year_diff    