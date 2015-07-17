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
df = pd.read_csv("run\\SimResults.csv")
df = df.describe()
df.to_csv("run\\SimStatsPandas.csv")