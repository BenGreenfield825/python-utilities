# Python Utilities
# by Ben Greenfield

from colorama import Fore
from colorama import Style

# --- Options --- #
LOG_FILE = "log.txt"
LOG_RW_MODE = 'a'   # default read-write mode is append
# --------------- #


# pass info into function to have it written to a log file
def write_to_log(info_to_write):
    file = open(LOG_FILE, LOG_RW_MODE)
    if file:
        file.write(str(info_to_write) + '\n')  # newline character added by default
    else:
        print(f"{Fore.BLUE}ERROR: Could not open log file!{Style.RESET_ALL}")
    file.close()

