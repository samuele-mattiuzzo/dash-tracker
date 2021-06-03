#!/bin/bash/python3

import calendar
import re
import sys
from datetime import datetime as dt
from datetime import timedelta
import pathlib

#//////////////// SETTINGS ///////////////////

empty_days = " -  "                       # Define what will be inserted for days not in month
calendar.setfirstweekday(calendar.MONDAY) # Define start of the week

#/////////////////////////////////////////////

# Markdown the month heading
month_header = "## " + month_text + "\n\n"

# Markdown the result headers
List_header = []
table_header = calendar.weekheader(3)
table_header = re.sub("(\w{3})", "|"+ r" \1" + "", table_header)

List_header.append(month_header)
List_header.append(table_header + "|\n")
List_header.append("|-----|-----|-----|-----|-----|-----|----|")

def Stringify(input_seq, seperator):
    return seperator.join(input_seq)

List_row = []
for row in calendar.monthcalendar(year,month):
    
    for days in row:
        day_string = '%d'%days

        if int(day_string) is 0:
            day_string = "|" + empty_days
        else:
            pass
        
        List_row.append(day_string)
    List_row.append('|\n')
    
Calendar = Stringify(List_header,' ') + "\n"
Calendar = Calendar + Stringify(List_row,' ')

# PRINT CALENDAR (WHEN RUNNING IN TERMINAL)
print(Calendar)              
