# -------------------- #
# Python Utilities
# by Ben Greenfield
# Co-authored by Ben Placzek
# -------------------- #
import os
import uuid
import datetime
import time
from colorama import Fore
from colorama import Style

# --- Options --- #
LOG_FILE = "log.txt"  # default log name (also acts as location)
LOG_RW_MODE = 'a'  # default read-write mode is append
LOG_DATETIME = "%x %X"  # default is (local date, local time)
NAME = "Ben Greenfield"  # "Ben Placzek"
# --------------- #

# TODO: update methods with proper docstrings


def set_log_path(log_path):
    """
    Use to set path to log file. End path with '/'.
    :param log_path:
    :return: none
    """
    global LOG_FILE
    LOG_FILE = log_path


# pass info into function to have it written to a log file
def write_to_log(info_to_write):
    """
    Pass info to write it to a log
    :param info_to_write:
    :return: none
    """
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


# gives a unique stamp to each file in a directory
def rename_with_stamp(path, stamp):
    for filename in os.listdir(path):
        my_dest = path + stamp + "_" + filename
        os.rename(path + filename, my_dest)


#  give each file in a directory a unuid name
# all files in directory must be the given fileType
def uniquify_files(path, fileType):
    for filename in os.listdir(path):
        my_dest = path + str(uuid.uuid1()) + "." + fileType
        os.rename(path + filename, my_dest)


# gets total size of directory, needs full file path to work
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


# file will be cleared out and written to with a
# listing of all the file names and the count at the bottom
def directory_report(path, write_to):
    count = 0

    open(write_to, "w").close()  # clear file
    f = open(write_to, "a")
    for x in os.listdir(path):
        f.write(x + '\n')
        count = count + 1
    f.write("\nNumber of files: " + str(count) + '\n')
    f.write("Size: " + str(get_size(path) / 1e+9) + ' GB')
    f.close()
