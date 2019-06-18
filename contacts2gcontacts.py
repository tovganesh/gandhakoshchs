#
# contacts2gcontacts.py - convert the plain contacts file to Google contacts format
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import sys
import csv
import argparse
import utils
import constants

def readInput(fileName):
    with open(fileName, 'rb') as csvfile:
        contactsReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        contactList = []
        for contact in contactsReader:            
            contactList.append(contact)    

        return contactList

def transformData(contactsData):
    transformedContactsData = []

    for contact in contactsData:
        flatID = contact[constants.GANDHKOSH_FIELDS["Flat ID"]]
        building, flatNo = flatID[0], flatID[1:]   # building and flat number
        
        owner = contact[constants.GANDHKOSH_FIELDS["Owner"]].strip()        
        if (owner.lower() == constants.REFUGEE): continue
        firstName, secondName = owner.split(" ")  # first and second name        

        email = contact[constants.GANDHKOSH_FIELDS["E-Mail"]]  # email

        mobile = contact[constants.GANDHKOSH_FIELDS["Mobile"]]  # mobile

        alternateEmail = contact[constants.GANDHKOSH_FIELDS["Alternate E-mail"]]  # alternate email

        alternateMobile = contact[constants.GANDHKOSH_FIELDS["Alternate Mobile"]]  # alternate mobile

        print(building, flatNo, firstName, secondName, email, mobile, alternateEmail, alternateMobile)

        # contacts are named on the building and flat number, and the owner name is added in organization field
        googleContact = {}
        googleContact[constants.GOOGLE_FIELDS["Name"]] = building + " " + flatNo
        googleContact[constants.GOOGLE_FIELDS["Given Name"]] = building
        googleContact[constants.GOOGLE_FIELDS["Family Name"]] = flatNo
        googleContact[constants.GOOGLE_FIELDS["Notes"]] = constants.OWNER
        googleContact[constants.GOOGLE_FIELDS["Group Membership"]] = constants.OWNER + " " + building + " ::: * myContacts"
        googleContact[constants.GOOGLE_FIELDS["E-mail 1 - Type"]] = "* Home"
        googleContact[constants.GOOGLE_FIELDS["E-mail 1 - Value"]] = email
        googleContact[constants.GOOGLE_FIELDS["Phone 1 - Type"]] = "Main"
        googleContact[constants.GOOGLE_FIELDS["Phone 1 - Value"]] = mobile
        googleContact[constants.GOOGLE_FIELDS["Phone 2 - Type"]] = "Other"
        googleContact[constants.GOOGLE_FIELDS["Phone 2 - Value"]] = alternateMobile
        googleContact[constants.GOOGLE_FIELDS["Organization 1 - Name"]] = secondName  # this is a trick
        googleContact[constants.GOOGLE_FIELDS["Organization 1 - Title"]] = firstName  # this is a trick

        transformedContactsData.append(googleContact)

    return transformedContactsData

def writeOutput(contactsData, fileName):
    googleContactFields = [constants.GOOGLE_FIELDS["Name"], constants.GOOGLE_FIELDS["Given Name"], constants.GOOGLE_FIELDS["Family Name"], GOOGLE_FIELDS["Notes"], \
                           constants.GOOGLE_FIELDS["Group Membership"], constants.GOOGLE_FIELDS["E-mail 1 - Type"], constants.GOOGLE_FIELDS["E-mail 1 - Value"], \
                           constants.GOOGLE_FIELDS["Phone 1 - Type"], constants.GOOGLE_FIELDS["Phone 1 - Value"], \
                           constants.GOOGLE_FIELDS["Phone 2 - Type"], constants.GOOGLE_FIELDS["Phone 2 - Value"], \
                           constants.GOOGLE_FIELDS["Organization 1 - Name"], constants.GOOGLE_FIELDS["Organization 1 - Title"]]
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=googleContactFields)

        writer.writeheader()
        for contact in contactsData:
            writer.writerow(contact)

def processCommandline():
    parser = argparse.ArgumentParser(description='Convert to Google CSV format')
    parser.add_argument('--input', type=str, required=True, help='input contacts CSV - Gandhakosh format')
    parser.add_argument('--output', type=str, required=True, help='output contacts CSV - Google format')

    return vars(parser.parse_args())

def main():
    args = processCommandline()
    contactsData = readInput(args['input'])
    transformedContactsData = transformData(contactsData)
    writeOutput(transformedContactsData, args['output'])

if __name__=="__main__":
    main()

