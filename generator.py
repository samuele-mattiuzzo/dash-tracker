#!/bin/bash/python3

import calendar, re
import os

CURRENT_DIR = os.getcwd()  # cwd
LOGS_DIR =  os.path.join(CURRENT_DIR, "logs")  # where to write the logs
calendar.setfirstweekday(calendar.MONDAY) # Define start of the week

def _build_dir(base_dir, pth):
    return os.path.join(base_dir, str(pth))

def _stringify(input_seq, seperator):
    return seperator.join(input_seq)

def _build_file(fname):
    return str(fname) + ".md"

year = 2021
month = 7
empty_days = " "

_start_folder = _build_dir(LOGS_DIR, year)
if not os.path.exists(_start_folder):
    os.mkdir(_start_folder)

# Markdown the result headers
header = []
header.append("| Phase")
_table_header = calendar.weekheader(3)
_table_header = re.sub(
    "(\w{3})",
    "|"+ r" \1" + "",
    _table_header)
header.append(_table_header + "|\n")
header.append("|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|")

while month <= 12:
    table_row = []  # The table row
    logs = []  # The log entries

    # populate the month
    for week in calendar.monthcalendar(year, month):
        table_row.append('| ')
        for days in week:

            # the table
            days = '%d' % days
            if int(days) is 0:
                day_string = "|" + empty_days
            else:
                name = calendar.day_abbr[calendar.weekday(
                    year, month, int(days)
                )].lower()
                day_string = '| [%s](#%s)' % (days, days)
                
                # the log entry
                log_entry = "### %s" % days + "\n" + "*%s -*" % name + "\n" +"\n"
                logs = [log_entry] + logs  # always insert at the top
        
            table_row.append(day_string)
        table_row.append('|\n')

    page = _stringify(header, '') + "\n"
    page = page + _stringify(table_row, '') + "\n" + "\n"
    page = page + _stringify(logs, '') + "\n"

    # write in the new file /month.md
    new_file = _build_file(month)
    with open(os.path.join(_start_folder, new_file), 'w') as tmp:
        tmp.write(page)
    tmp.close()

    # next month
    page = ''
    month += 1
