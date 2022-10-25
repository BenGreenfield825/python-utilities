# -------------------- #
# Python Utilities
# by Ben Greenfield
# Co-authored by Ben Placzek
# -------------------- #

import datetime
import time
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


# takes an initial format argument followed by any number of data args
# formats and prints an error message then exits
def fatal(format, *argv):
    print(f"{Fore.RED}" + str(format) + f"{Style.RESET_ALL}")
    for x in argv:
        print(f"{Fore.RED}" + str(x) + f"{Style.RESET_ALL}")
    quit()


# delays a specified number of seconds, rounds up to the nearest integer
# second argument optional
def delay(seconds, debug_comments=False):
    counter = 0
    while counter < seconds:
        counter += 1
        if debug_comments:
            print(counter)
        time.sleep(1)


# used to check if the given "item" is none type or is empty
# second argument optional
def is_none_or_empty(item, debug_comments=False):
    if item is None:
        if debug_comments:
            print(f"{Fore.YELLOW}" + "Item is None")
        return True
    elif item == "":
        if debug_comments:
            print(f"{Fore.YELLOW}" + "Item is empty")
        return True
    else:
        if debug_comments:
            print(f"{Fore.RED}" + "Item is neither none nor empty")
        return False

