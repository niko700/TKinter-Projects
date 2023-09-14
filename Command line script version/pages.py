#-------------------------------------------------------------------------------
# Name:          Reading Percent 
# Purpose:       Estimates percent currently read of a large document.
#                This is the one parameter version, and total pages are hard-coded in
#
# To Run:        Command-line version --> run script in Command Prompt
#                Format: "python scriptname.py your_page_number"
#
# Author:        niko700
# Created:       01/09/2023 --> Euro date
# Copyright:     (c) niko700 2023
# Licence:       <your licence>

# Edits: 09/02/23
#        09/13/23    - edited caption
#-------------------------------------------------------------------------------


from sys import argv

#enter number of pages in document
#***MANUAL ENTRY***
all_pages = 75

#function to find percent
def percent(string="1"):

    number = int(string)
    total = number/all_pages*100
    return print(str(round(total,2)) + " %")


if __name__ == '__main__':
    percent(*argv[1:])

