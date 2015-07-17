#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jurong
#
# Created:     17/07/2015
# Copyright:   (c) Jurong 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile)
    df = df.describe()
    df.to_csv(ofile)

getSimStats(sys.argv[1], sys.argv[2])