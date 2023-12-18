import numpy as np
import pandas as pd

def input_raw_data(features_dict):
    input = pd.read_excel('../data/Rawdata.xlsx',header = 1)
    for i in range(439):
        for feature in features_dict:
            j = 0
            features_dict[feature].extend(float(input.iloc[j + i*9,6]))
            j += 1
    return features_dict