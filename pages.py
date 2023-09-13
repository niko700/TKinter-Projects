#-------------------------------------------------------------------------------
# Name:        Reading Percent
# Purpose:     Estimates percent currently read of a large document.
#
# Author:      vnner
#
# Created:     01/09/2023 --> Euro date
# Copyright:   (c) vnner 2023
# Licence:     <your licence>

#Edits: 09/02/23
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

