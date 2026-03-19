'''
Student Names: Zach, Nhu
Date:
'''

import os
import pandas as pd
import sys


def split_data(df, test_size = 0.3, random_state=42):
    df = df.sample(frac=1, random_state = random_state).reset_index(drop=True) #drop = True

    split_index = int((1-test_size)*len(df))

    train_df = df[:split_index]
    test_df = df[split_index:]

    return train_df, test_df

if len(sys.argv) < 2:
    print(f"This file is used like this: python3 {__file__} cleaner.csv")
    quit()


input_file = sys.argv[1]

df = pd.read_csv(input_file)

train_df, test_df = split_data(df, test_size = 0.3)

#output files
train_df.to_csv("train.csv", index=False)
test_df.to_csv("test.csv", index=False)

print(f"exported train.csv to 70% and test.csv to 30%")