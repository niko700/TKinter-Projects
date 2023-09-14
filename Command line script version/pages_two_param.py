#-------------------------------------------------------------------------------
# Name:         Reading Percent
# Purpose:      Estimates percent currently read of a large document.
#               This is the two-parameter version.
#               Has default values hard-coded in, in case user does not provide parameters
#
# To Run:       Command-line version --> run script in Command Prompt
#               Format: "python scriptname.py your_page_number total_pages"
#
# Author:       niko700
# Created:      01/09/2023 --> Euro date
# Copyright:    (c) niko700 2023
# Licence:      <your licence>

# Edits: - 09/02/23
#       - 09/13/23 - added second parameter for total pages
#-------------------------------------------------------------------------------


from sys import argv

#function to find percent reading progress
#two parameters: (1) page you're on now, and (2) total pages
#enter in command line; parameters that you enter this way are in string format
def percent(current_page_string="1", total_pages_string="100"):

    #convert input numbers (strings) to integers
    current_page_int = int(current_page_string)
    total_pages_int = int(total_pages_string)
    
    #calculate percent
    percent_progress = current_page_int/total_pages_int*100
    return print(str(round(percent_progress,2)) + " %")


if __name__ == '__main__':
    percent(*argv[1:])

