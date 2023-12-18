import numpy as np

def divide_data(features,truth):
    features = np.array(features)
    x_test_data = features[259:346]   
    x_train_data = np.delete(features,np.s_[259:346],axis = 0)
    truth_test = truth[259:346]
    truth_train = np.delete(truth,np.s_[259:346],axis = 0)
    truth_train = np.mat(truth_train) 
    y_train_data = np.transpose(truth_train).A 
    truth_test = np.mat(truth_test)  
    y_test_data = np.transpose(truth_test).A 
    return x_test_data,x_train_data,y_train_data,y_test_data