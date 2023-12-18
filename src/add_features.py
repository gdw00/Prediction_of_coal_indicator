import numpy as np

def add_features(x_test_data_pca,x_train_data_pca,x_test_data_yuan,x_train_data_yuan):
    x_test_all = np.hstack((x_test_data_yuan,x_test_data_pca))
    x_train_all = np.hstack((x_train_data_yuan,x_train_data_pca))
    return x_test_all,x_train_all