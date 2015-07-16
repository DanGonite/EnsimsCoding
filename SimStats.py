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
y = 17
minlist = ["Min"]
maxlist = ["Max"]
meanlist = ["Mean"]

with open('F:\Things\Programming\Ensims Coding\SimResults.csv', 'rb') as csvfile:   # Change file path as necessary
    header = csv.Sniffer().has_header(csvfile.read())
    csvfile.seek(0)
    reader = list(csv.reader(csvfile))
    for n in range(y):
        value = []
        csvfile.seek(0)
        for row in reader:
            if n > 18:
                break
            try:
                data = float(row[0])
                value.append(data)
                break
            except ValueError:
                n += 1
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
with open('F:\Things\Programming\Ensims Coding\SimStats.csv', "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(minlist)
    writer.writerow(maxlist)
    writer.writerow(meanlist)


