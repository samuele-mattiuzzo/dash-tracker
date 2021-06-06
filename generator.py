#!/bin/bash/python3

import calendar, re
import os

CURRENT_DIR = os.getcwd()  # cwd
LOG_MD = os.path.join(CURRENT_DIR, "log.md")
LOGS_DIR =  os.path.join(CURRENT_DIR, "logs")  # where to write the logs
calendar.setfirstweekday(calendar.MONDAY) # Define start of the week

def _build_dir(base_dir, pth):
    return os.path.join(base_dir, str(pth))

def _stringify(input_seq, seperator):
    return seperator.join(input_seq)

def _build_file(fname):
    return str(fname) + ".md"

# starting defaults
year = 2022
month = 1
empty_days = " "

_start_folder = _build_dir(LOGS_DIR, year)
if not os.path.exists(_start_folder):
    os.mkdir(_start_folder)

# Links in log.md
links = []
links.append("- {}\n".format(year))

# Markdown the result headers
header = []
header.append("| Phase")
_table_header = calendar.weekheader(3)
_table_header = re.sub("(\w{3})", "|"+ r" \1" + "", _table_header)
header.append(_table_header + "|\n")
header.append("|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|")

while month <= 1:
    # updates the link in reverse order
    links.insert(1, "  - [{}](logs/{}/{}.md)\n".format(month, year, month))

    table_row = []  # the table row
    logs = []  # the log entries

    # populate the month
    for week in calendar.monthcalendar(year, month):
        table_row.append('| ')
        for days in week:

            # the table
            days = int(days)
            if days is 0:
                day_string = "|" + empty_days
            else:
                day_string = '| [{}](#{}) '.format(days, days)
                
                # the log entry
                name = calendar.day_abbr[calendar.weekday(
                    year, month, days
                )].lower()
                log_entry = "### {}\n*{} -*\n\n".format(days, name)
                logs = [log_entry] + logs  # always insert at the top
        
            table_row.append(day_string)
        table_row.append('|\n')

    # build the new log page with the calendar
    page = _stringify(header, '') + "\n"
    page = page + _stringify(table_row, '') + "\n" + "\n"
    page = page + _stringify(logs, '') + "\n"


    # write in the new file /month.md
    new_file_path = os.path.join(_start_folder, _build_file(month))
    if not os.path.exists(new_file_path):
        with open(new_file_path, 'w') as tmp:
            tmp.write(page)
        tmp.close()

    # next month
    page = ''
    month += 1

# updates the log index
with open(LOG_MD, 'r+') as log_md:
    content = log_md.read()
    log_md.seek(0, 0)
    log_md.write(
        _stringify(links, '') + "\n" + content
    )
log_md.close()
