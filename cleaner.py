'''
Student Names: Zach, Nhu
Date:
'''

import os
import pandas as pd
import sys

# Verify commandline arguments

if len(sys.argv) < 2:
    print(f"This file is used like this: 'python3 {__file__} [data.csv]'")
    quit()

# Load the file

dtype: dict = {
    "System Trans. ID": str,
    "HHID": str,
    "GeoID": str,
    "Trans Date": str,
    "Distinct Pro": str,
    "Basket Units": str,
    "Basket Dollar": str,
    "Day-of-Week": str,
    "Family Size": str,
    "Race": str,
    "Income": str,
    "Home Ownership": str,
    "Male Education": str,
    "Male Occupation": str,
    "Female Age": str,
    "Female Work": str,
    "Chldrn 0-5": str,
    "Chldrn 6-11": str,
    "Chldrn 12-17": str,
    "Markets": str,
    "Chains": str,
    "Outlets": str,
    "UPC": str,
    "UPC Description": str,
    "Category": str,
    "Vendor": str,
    "Brand": str,
    "SKU Dollars": str,
    "SKU Units": str,
    "Size": str,
    "SizeUnit": str,
    "": str,
    "": str,
    "": str,
    "": str
}

df = pd.read_csv(sys.argv[1], dtype=dtype)

# Remove NaN values

df = df.dropna()
print(df)

# Remove columns with only one unique value
