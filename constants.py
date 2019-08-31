#
# constants.py - various constants used in the scripts for gchs
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

import utils

# google format
GOOGLE_FIELDS = utils.listToDict(["Name", "Given Name", "Additional Name", "Family Name", "Yomi Name", "Given Name Yomi", "Additional Name Yomi",
                                  "Family Name Yomi", "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name", "Maiden Name", "Birthday",
                                  "Gender", "Location", "Billing Information", "Directory Server", "Mileage", "Occupation", "Hobby", "Sensitivity",
                                  "Priority", "Subject", "Notes", "Language", "Photo", "Group Membership", "E-mail 1 - Type", "E-mail 1 - Value",
                                  "Phone 1 - Type", "Phone 1 - Value", "Phone 2 - Type", "Phone 2 - Value", "Organization 1 - Type",
                                  "Organization 1 - Name", "Organization 1 - Yomi Name", "Organization 1 - Title", "Organization 1 - Department",
                                  "Organization 1 - Symbol", "Organization 1 - Location", "Organization 1 - Job Description"])

# gandhakosh format
GANDHKOSH_FIELDS = utils.listToDict(
    ["Flat ID", "Owner", "E-Mail", "Mobile", "IsIndiaMobile", "Alternate E-mail", "Alternate Mobile"])

# refugee
REFUGEE = "refugee"

# owner
OWNER = "Owner"

# DB name
GANDHAKOSH_DB = "data/gandhakoshchs.db"
