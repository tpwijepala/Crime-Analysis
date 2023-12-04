import os
import pandas as pd
import numpy as np
from scipy import stats

# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/"+file)
    df = pd.concat([df, data])