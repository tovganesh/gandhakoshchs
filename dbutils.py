#
# dbutils.py - various DB utility functions used in the scripts for gchs
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import sqlite3
import constants

# connect to db


def dbConnect(dbName=constants.GANDHAKOSH_DB):
    db = sqlite3.connect(dbName)
    cursor = db.cursor()

    return db, cursor

# check if table exists


def doesTableExist(cursor, tableName):
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name=:table_name"
    cursor.execute(sql, {"table_name": tableName})
    return len(cursor.fetchall()) > 0

# create a table if not exist


def createTable(db, cursor, tableName, fields, forceDelete=False):
    tableExist = doesTableExist(cursor, tableName)
    if (forceDelete and tableExist):
        sql = "DROP TABLE " + tableName
        cursor.execute(sql)
        db.commit()

    tableExist = doesTableExist(cursor, tableName)

    # check if table exists
    if (tableExist):
        return False  # can't make it

    # make the table
    if (type(fields) != 'tuple'):
        fields = tuple(fields)
    sql = "CREATE TABLE " + tableName + " " + repr(fields)
    cursor.execute(sql)
    db.commit()

    return True
