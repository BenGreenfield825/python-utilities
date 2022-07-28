# -------------------- #
# Python Utilities
# by Ben Greenfield
# -------------------- #

import datetime
from colorama import Fore
from colorama import Style

# --- Options --- #
LOG_FILE = "log.txt"
LOG_RW_MODE = 'a'   # default read-write mode is append
LOG_DATETIME = "%x %X"  # default is (local date, local time)
NAME = "Ben Greenfield"
# --------------- #


# pass info into function to have it written to a log file
def write_to_log(info_to_write):
    file = open(LOG_FILE, LOG_RW_MODE)
    if file:
        date = "(" + datetime.datetime.now().strftime(LOG_DATETIME) + ") "
        file.write(date + str(info_to_write) + '\n')  # newline character added by default
    else:
        print(f"{Fore.RED}ERROR: Could not open log file!{Style.RESET_ALL}")
    file.close()


# print name and date
def banner():
    print("--------------------------")
    print(NAME + '\t' + str(datetime.datetime.today().date()))
    print("--------------------------")


# print a termination message
def bye():
    print("--------------------------")
    print("Normal Termination")
    print("--------------------------")

