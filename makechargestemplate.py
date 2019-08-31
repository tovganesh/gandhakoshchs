#
# makechargestemplate.py - make charges template for ApnaComplex import
#
# @author V. Ganesh
# @date 31st August 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import argparse
import utils
import json
import csv

chargesDataFields = ["Block", "Unit", "Charge Type", "Charge Description", "Charge Date", "Pay By Date(optional)", "Amount"]

def processCommandline():
    parser = argparse.ArgumentParser(
        description='Charges template for ApnaComplex import')
    parser.add_argument('--input', type=str, required=True,
                        help='CSV sheet with unit occupany')
    parser.add_argument('--charges', type=str, required=True,
                        help='JSON file with charge heads') 
    parser.add_argument('--month', type=str, required=True,
                        help='integer month, 1=Jan, 2=Feb .. 12=Dec') 
    parser.add_argument('--year', type=str, required=True,
                        help='year, say 2019') 
    parser.add_argument('--chargeday', type=str, required=False, default="1",
                        help='the charge day') 
    parser.add_argument('--dueday', type=str, required=False, default="10",
                        help='the due day') 
    parser.add_argument('--output', type=str, required=True,
                        help='CSV output for ApnaComplex import') 
    return vars(parser.parse_args())

def writeOutput(chargesData, fileName):
    global chargesDataFields

    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=chargesDataFields)

        writer.writeheader()
        for cd in chargesData:
            writer.writerow(cd)

def transformToApnaComplexFormat(occupancyRecord, chargesData, month, year, chargeDay, dueDay):
    global chargesDataFields

    transformedRecords = []

    allApplicable = filter(lambda x: x["applicable"]=="all", chargesData)

    for applicable in allApplicable:
      print("applicable", applicable)
      rec = utils.listToDict(chargesDataFields)
      rec["Block"] = occupancyRecord["Block"]
      rec["Unit"]  = occupancyRecord["Unit"]
      rec["Charge Type"] = applicable["head"]
      rec["Charge Description"] = applicable["description"] + " FOR " + utils.monthToShort(month) + " " + year
      rec["Charge Date"] = chargeDay + "/" + month + "/" + year
      rec["Pay By Date(optional)"] = dueDay + "/" + month + "/" + year
      rec["Amount"] = applicable["charge"]

      transformedRecords.append(rec)

    if (occupancyRecord["Residing"] == "N"):
       allApplicable = filter(lambda x: x["applicable"]=="rented", chargesData)

       for applicable in allApplicable:
         print("applicable", applicable)
         rec = utils.listToDict(chargesDataFields)
         rec["Block"] = occupancyRecord["Block"]
         rec["Unit"]  = occupancyRecord["Unit"]
         rec["Charge Type"] = applicable["head"]
         rec["Charge Description"] = applicable["description"] + " FOR " + utils.monthToShort(month) + " " + year
         rec["Charge Date"] = chargeDay + "/" + month + "/" + year
         rec["Pay By Date(optional)"] = dueDay + "/" + month + "/" + year
         rec["Amount"] = applicable["charge"]

         transformedRecords.append(rec)

    return transformedRecords

def main():
    args = processCommandline()
    occupancyData = utils.readCSV(args['input'])
    chargesData   = json.loads(open(args['charges']).read())

    print(chargesData)

    month = args['month']
    year  = args['year']
    chargeDay = args['chargeday']
    dueDay = args['dueday']
   
    transformedRecords = [] 
    for ocd in occupancyData:
       if (ocd['Residing'] == ''): continue # refugee flat, ignore
       trec = transformToApnaComplexFormat(ocd, chargesData, month, year, chargeDay, dueDay)
       print(ocd, trec)

       for rec in trec:
         transformedRecords.append(rec)

    writeOutput(transformedRecords, args['output'])

if __name__ == "__main__":
    main()
