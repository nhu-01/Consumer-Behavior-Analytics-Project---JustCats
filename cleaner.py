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
    "System Trans. ID": int,
    "HHID": int,
    "GeoID": int,
    "Trans Date": str,
    "Distinct Pro": int,
    "Basket Units": int,
    "Basket Dollar": float,
    "Day-of-Week": str,
    "Family Size": int,
    "Race": str,
    "Income": int,
    "Home Ownership": str,
    "Male Education": int,
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
    "Category": int,
    "Vendor": str,
    "Brand": str,
    "SKU Dollars": str,
    "SKU Units": str,
    "Size": float,
    "SizeUnit": int,
    "Unnamed: 31": int,
    "Unnamed: 32": str,
    "Unnamed: 33": str,
    "Unnamed: 34": str
}

df = pd.read_csv(sys.argv[1], dtype=dtype)

# Remove NaN values

df = df.dropna()

# Remove columns with only one unique value
