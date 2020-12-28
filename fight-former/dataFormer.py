# sort by fight Id
# Find winner and store as result
# For Fighter AB
#   f get last 10 rounds
#     if no 10 rounds omit fight
#     else store 10 rounds

#python 3.6.9

import re
import ufcstats
import fighter
from fighter import Fighter
import json
import csv

def getFighterStats(name):
    stats = ufcstats.getStats(name)
    return stats

def trimNonNum(strang):
    return int( re.sub("[^0-9]", "", strang ))

def trimNewLine(strang):
    return strang.replace("\n", "").replace("'", "")

def heightToInches(height):
    array = height.split("'")
    feetInInches = trimNonNum(array[0]) * 12
    inches = trimNonNum(array[1])
    return (feetInInches + inches)

def stanceVal(stance):
    if stance == "Orthodox":
        return 0
    elif stance == "Southpaw":
        return 1
    elif stance == "Switch":
        return 2
    else:
        print("error in stance name: "+stance)
        quit()

stats = json.loads(getFighterStats("Conor McGregor"))
print(stats)
# quit()

dan = Fighter(
    stats["Name"],
    heightToInches(stats["Height:"]),
    trimNonNum(stats["Weight:"]),
    trimNonNum(stats["Reach:"]),
    stanceVal(stats["STANCE:"]),
    stats["DOB:"][-4:]
    )
text_file = open("fighterName.txt", "r")
lines = text_file.readlines()
text_file.close()

fighterStats = []
for name in lines:
    stats = json.loads(getFighterStats(name))
    try:
        fighter = Fighter(
            stats["Name"],
            heightToInches(stats["Height:"]),
            trimNonNum(stats["Weight:"]),
            trimNonNum(stats["Reach:"]),
            stanceVal(stats["STANCE:"]),
            stats["DOB:"][-4:]
        )
        fighterStats.append(fighter)
    except Exception as e:
        print("skipping ", name)
