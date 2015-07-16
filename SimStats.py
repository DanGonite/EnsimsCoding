#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jurong
#
# Created:     15/07/2015
# Copyright:   (c) Jurong 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv

n=0
y = 19
minlist = ["Min", ""]
maxlist = ["Max", ""]
meanlist = ["Mean", ""]
headlist = []

with open('run\SimResults.csv', 'rb') as csvfile:   # Change file path as necessary
    header = csv.Sniffer().has_header(csvfile.read())
    csvfile.seek(0)
    reader = list(csv.reader(csvfile))
    for item in reader[0]:
        headlist.append(item)
    for n in range(y):
        value = []
        csvfile.seek(0)
        for row in reader:
            if n > 18:
                break
            try:
                data = float(row[n])
                value.append(data)
            except ValueError:
                pass
        try:
            minlist.append(min(value))
            maxlist.append(max(value))
            mean = 0
            for item in value:
                mean += item
            mean /= len(value)
            meanlist.append(mean)
        except ValueError:
            pass
    minlist[2] = ""
    maxlist[2] = ""
    meanlist[2] = ""
with open('run\SimStats.csv', "wb") as csvfile: # Change file path as necessary
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(headlist)
    writer.writerow(minlist)
    writer.writerow(maxlist)
    writer.writerow(meanlist)



