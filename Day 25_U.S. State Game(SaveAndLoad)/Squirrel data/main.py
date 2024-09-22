import csv
import pandas
from collections import defaultdict

#Constant
INPUT_DIR = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT_DIR = "squirrel_count.csv"


#Read data
squirrel_data = pandas.read_csv(INPUT_DIR)

#Add to data to dict
squirrel_color = defaultdict(int)
for color in squirrel_data["Primary Fur Color"]:
        #Blank value
        if pandas.notna(color):
            squirrel_color[color] += 1

#SETUP HEADER AND ROWS
FIELD_NAMES = ["Fur Color", "Count"]
ROWS = [{"Fur Color": Color, "Count": Value} for Color, Value in squirrel_color.items()]


with open(OUTPUT_DIR, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames= FIELD_NAMES)
    writer.writeheader()
    writer.writerows(ROWS)