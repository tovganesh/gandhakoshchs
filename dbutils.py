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
def dbConnect(dbName = constants.GANDHAKOSH_DB):
    db = sqlite3.connect(dbName)
    cursor = db.cursor()

    return db, cursor

# check if table exists
def doesTableExist(cursor, tableName):
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='?'"
    cursor.execute(sql, (tableName,))
    return len(cursor.fetchall()) > 0

# create a table if not exist 
def createTable(db, cursor, tableName, fields, forceDelete=False):
    if (forceDelete):
        sql = "DROP TABLE tableName"
        cursor.execute(sql)
        db.commit()

    # check if table exists
    if (doesTableExist(cursor, tableName)):
        return False # can't make it

    # make the table
    sql = "CREATE TABLE ? ?"
    cursor.execute(sql, (tableName, fields))
    db.commit()

    return True
    


