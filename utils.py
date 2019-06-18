#
# utils.py - various utility functions used in the scripts for gchs
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import csv

# convet a list to a dict
def listToDict(list):
    dict = {}
    for li in list:
        dict[li] = li
    return dict

# read a CSV (comma delimited, with " as quote char) and return a list of row in the file
def readCSV(fileName):
    with open(fileName, 'rb') as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        data = []
        for row in csvReader:            
            data.append(row)    

        return data
