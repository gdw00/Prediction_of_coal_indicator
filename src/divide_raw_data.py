import numpy as np

def divide_raw_data(features_dict):
    test_features_dict={'feature1':[],'feature2':[],'feature3':[],'feature4':[],'feature5':[],'feature6':[],'feature7':[],'feature8':[],'feature9':[]}
    train_features_dict={'feature1':[],'feature2':[],'feature3':[],'feature4':[],'feature5':[],'feature6':[],'feature7':[],'feature8':[],'feature9':[]}
    for feature in features_dict:
        test_features_dict[feature]=np.mat(features_dict[feature][0:87])
        train_features_dict[feature]=np.mat(features_dict[feature][87:439])

    in_train = np.vstack((train_features_dict['feature1'],train_features_dict['feature2'],train_features_dict['feature3'],
                           train_features_dict['feature4'],train_features_dict['feature5'],train_features_dict['feature6'],
                           train_features_dict['feature7'],train_features_dict['feature8'],train_features_dict['feature9'])) 
    in_train_t = np.transpose(in_train).A 

    in_test = np.vstack((test_features_dict['feature1'],test_features_dict['feature2'],test_features_dict['feature3'],
                          test_features_dict['feature4'],test_features_dict['feature5'],test_features_dict['feature6'],
                          test_features_dict['feature7'],test_features_dict['feature8'],test_features_dict['feature9'],)) 
    in_test_t = np.transpose(in_test.A) 

    all = np.vstack((in_test_t,in_train_t))
    all = np.array(all)
    x_test_data = all[259:346]   
    x_train_data = np.delete(all,np.s_[259:346],axis = 0)
    return x_test_data,x_train_data