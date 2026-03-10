'''
Student Names: Zach, Nhu
Date:
'''

import os
import pandas as pd
import sys

# Verify commandline arguments

if len(sys.argv) < 3:
    print(f"This file is used like this: 'python3 {__file__} [data.csv]'")

# Load the file

df = pd.read_csv(sys.argv[2])

# Remove NaN values

df = df.dropna()

# Remove columns with only one unique value
