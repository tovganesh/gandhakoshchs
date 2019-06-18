#
# utils.py - various utility functions used in the scripts for gchs
#
# @author V. Ganesh
# @date 2nd June 2019
# @license GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
#
# (c) V. Ganesh
#

# convet a list to a dict
def listToDict(list):
    dict = {}
    for li in list:
        dict[li] = li
    return dict