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

import csv, math, sys

def getSimStats(ifile, ofile):
    minlist = ["Min", ""]
    maxlist = ["Max", ""]
    meanlist = ["Mean", ""]
    stddevlist = ["Standard Deviation", ""]
    headlist = []

    with open(ifile, 'rb') as csvfile:   # Opens file as "read-able binary"
        reader = list(csv.reader(csvfile))  # Reads the file as a list
        for item in reader[0]:  # Loops through items in the first row (header) of the file
            headlist.append(item)   # Creates the Header row
    	y = len(headlist)  # Calculates the number of columns
        for n in range(y):  # Loops through columns in the file
            value = []  # Resets "Value" list to empty
            for row in reader:  # Loops through rows in the file
                try:
                    data = float(row[n])    # Sets "data" to the value of column "n" in the row as a decimal
                    value.append(data)  # Adds "data" to the list of "Values"
                except ValueError:  # Checks if an error has been returned
                    pass
            try:
                minlist.append(min(value))  # Calculates the minimum value in the "value" list and adds it to "minlist"
                maxlist.append(max(value))  # Calculates the maximum value in the "value" list and adds it to "maxlist"
                mean = 0
                for item in value:
                    mean += item
                mean /= len(value)   # Adds each item in the "value" list to "mean" and divides "mean" by the number of values that were added
                meanlist.append(mean)   # Adds "mean" to the list of means
                sumsq = 0
                for i in range(len(value)):
                	sumsq += (value[i] - mean) **2
                stddevlist.append(math.sqrt(sumsq/(len(value)-1)))
            except ValueError:  # Checks for an error
                pass
        minlist[2] = "" # Removes the 3rd entry (Job_Id)
        maxlist[2] = "" # Removes the 3rd entry (Job_Id)
        meanlist[2] = ""    # Removes the 3rd entry (Job_Id)
        stddevlist[2] = ""    # Removes the 3rd entry (Job_Id)

    with open(ofile, "wb") as csvfile:     # Opens file as "write-able" binary
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(headlist)   # }
        writer.writerow(minlist)    # }
        writer.writerow(maxlist)    # } Writes the data to a different document
        writer.writerow(meanlist)   # }
        writer.writerow(stddevlist) # }

getSimStats(sys.argv[1], sys.argv[2])

