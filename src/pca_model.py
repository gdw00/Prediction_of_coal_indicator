from sklearn.decomposition import PCA
import numpy as np

def pca_model(x_test_data,x_train_data):
    all = np.vstack((x_test_data,x_train_data))
    all = np.array(all)
    pca = PCA(n_components = 4)  #2 OR 'mle'
    pca = pca.fit(all) 
    result = pca.transform(all) 
    x2_test_data = result[259:346]   
    x2_train_data = np.delete(result,np.s_[259:346],axis = 0)
    return x2_test_data,x2_train_data,pca

