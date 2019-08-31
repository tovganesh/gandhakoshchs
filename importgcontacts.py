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
    parser = argparse.ArgumentParser(
        description='Import Google Contacts CSV to sql-lite')
    parser.add_argument('--input', type=str, required=True,
                        help='input contacts CSV - Google format')

    return vars(parser.parse_args())


def importData(db, cursor, contactsData, tableName):
    pass


def main():
    args = processCommandline()
    contactsData = utils.readCSV(args['input'])

    db, cursor = dbutils.dbConnect()
    dbutils.createTable(db, cursor, "Owner", ("building text", "flat_number text", "primary_first_name text", "primary_last_name text",
                                              "primary_email text", "primary_mobile text", "secondary_email text", "secondary_mobile text", "flat_type text"), True)

    importData(db, cursor, contactsData, "Owner")


if __name__ == "__main__":
    main()
