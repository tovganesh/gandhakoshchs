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

def listToDict(list):
    dict = {}
    for li in list:
        dict[li] = li
    return dict

# google format
GOOGLE_FIELDS = listToDict(["Name","Given Name","Additional Name","Family Name","Yomi Name","Given Name Yomi","Additional Name Yomi",\
                 "Family Name Yomi","Name Prefix","Name Suffix","Initials","Nickname","Short Name","Maiden Name","Birthday",\
                 "Gender","Location","Billing Information","Directory Server","Mileage","Occupation","Hobby","Sensitivity",\
                 "Priority","Subject","Notes","Language","Photo","Group Membership","E-mail 1 - Type","E-mail 1 - Value",\
                 "Phone 1 - Type","Phone 1 - Value","Phone 2 - Type","Phone 2 - Value","Organization 1 - Type",\
                 "Organization 1 - Name","Organization 1 - Yomi Name","Organization 1 - Title","Organization 1 - Department",\
                 "Organization 1 - Symbol","Organization 1 - Location","Organization 1 - Job Description"])

# gandhakosh format
GANDHKOSH_FIELDS = listToDict(["Flat ID","Owner","E-Mail","Mobile","IsIndiaMobile","Alternate E-mail","Alternate Mobile"])

# refugee
REFUGEE = "refugee"

# owner
OWNER = "Owner"

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
        flatID = contact[GANDHKOSH_FIELDS["Flat ID"]]
        building, flatNo = flatID[0], flatID[1:]   # building and flat number
        
        owner = contact[GANDHKOSH_FIELDS["Owner"]].strip()        
        if (owner.lower() == REFUGEE): continue
        firstName, secondName = owner.split(" ")  # first and second name        

        email = contact[GANDHKOSH_FIELDS["E-Mail"]]  # email

        mobile = contact[GANDHKOSH_FIELDS["Mobile"]]  # mobile

        alternateEmail = contact[GANDHKOSH_FIELDS["Alternate E-mail"]]  # alternate email

        alternateMobile = contact[GANDHKOSH_FIELDS["Alternate Mobile"]]  # alternate mobile

        print(building, flatNo, firstName, secondName, email, mobile, alternateEmail, alternateMobile)

        # contacts are named on the building and flat number, and the owner name is added in organization field
        googleContact = {}
        googleContact[GOOGLE_FIELDS["Name"]] = building + " " + flatNo
        googleContact[GOOGLE_FIELDS["Given Name"]] = building
        googleContact[GOOGLE_FIELDS["Family Name"]] = flatNo
        googleContact[GOOGLE_FIELDS["Notes"]] = OWNER
        googleContact[GOOGLE_FIELDS["Group Membership"]] = OWNER + " " + building + " ::: * myContacts"
        googleContact[GOOGLE_FIELDS["E-mail 1 - Type"]] = "* Home"
        googleContact[GOOGLE_FIELDS["E-mail 1 - Value"]] = email
        googleContact[GOOGLE_FIELDS["Phone 1 - Type"]] = "Main"
        googleContact[GOOGLE_FIELDS["Phone 1 - Value"]] = mobile
        googleContact[GOOGLE_FIELDS["Phone 2 - Type"]] = "Other"
        googleContact[GOOGLE_FIELDS["Phone 2 - Value"]] = alternateMobile
        googleContact[GOOGLE_FIELDS["Organization 1 - Name"]] = secondName  # this is a trick
        googleContact[GOOGLE_FIELDS["Organization 1 - Title"]] = firstName  # this is a trick

        transformedContactsData.append(googleContact)

    return transformedContactsData

def writeOutput(contactsData, fileName):
    googleContactFields = [GOOGLE_FIELDS["Name"], GOOGLE_FIELDS["Given Name"], GOOGLE_FIELDS["Family Name"], GOOGLE_FIELDS["Notes"], \
                           GOOGLE_FIELDS["Group Membership"], GOOGLE_FIELDS["E-mail 1 - Type"], GOOGLE_FIELDS["E-mail 1 - Value"], \
                           GOOGLE_FIELDS["Phone 1 - Type"], GOOGLE_FIELDS["Phone 1 - Value"], \
                           GOOGLE_FIELDS["Phone 2 - Type"], GOOGLE_FIELDS["Phone 2 - Value"], \
                           GOOGLE_FIELDS["Organization 1 - Name"], GOOGLE_FIELDS["Organization 1 - Title"]]
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

main()

