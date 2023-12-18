import numpy as np
import pandas as pd

def input_coal_data(features_dict):
    input_data= pd.read_excel('../data/Rawdata.xlsx',header =1)
    output_data=pd.read_excel("../data/Coaldata.xlsx",header =1)
    for i in range(439):
        input = []
        features_dict = {'feature1':[],'feature2':[],'feature3':[],'feature4':[],
                       'feature5':[],'feature6':[],'feature7':[],'feature8':[],'feature9':[]}
        for feature in features_dict:
            j = 0
            features_dict[feature].extend(input_data.iloc[j+i*9,13:61].values)
            input.extend(features_dict[feature])
            j += 1
        input_t=np.mat(input)   
        if i == 0:
            input_all=np.vstack((input_t))
        if i != 0:
            input_all=np.row_stack((input_all,input_t))
    out=output_data.iloc[:,4].values
    return input_all,out