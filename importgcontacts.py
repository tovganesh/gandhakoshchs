#
# importgcontacts.py - import Google Contacts csv file into a sql lite DB
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import argparse
import utils
import dbutils

def processCommandline():
    parser = argparse.ArgumentParser(description='Import Google Contacts CSV to sql-lite')
    parser.add_argument('--input', type=str, required=True, help='input contacts CSV - Google format')

    return vars(parser.parse_args())

def main():
    args = processCommandline()
    contactsData = utils.readCSV(args['input'])

    db, cursor = dbutils.dbConnect()
    dbutils.createTable(db, cursor, "User", ("name", "contact"))

if __name__=="__main__":
    main()

