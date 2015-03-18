#!/usr/bin/env python 
from dateutil import parser
import datetime

# inclusive
START_DATE = "3/27/15 9:00AM" 
END_DATE = "4/8/15 9:00PM" 

start = parser.parse(START_DATE)
end = parser.parse(END_DATE)

now = start
while True:
    dt_str = now.strftime("%-m/%-d (%a) ")
    dt_str += "morning" if now.hour < 12 else "evening" 
    print dt_str + ": __________________________"
    now += datetime.timedelta(hours=12)
    if now > end: break

