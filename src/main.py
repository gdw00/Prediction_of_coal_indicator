import joblib
from divide_raw_data import divide_raw_data
from input_raw_data import input_raw_data
from divide_data import divide_data
from test_val import test_val
from tree_model import tree_model
from logger import get_logger
from configparser import ConfigParser 
from input_coal_data import input_coal_data
from pca_model import pca_model
from add_features import add_features 


if __name__ == "__main__":
    features_dict={'feature1':[],'feature2':[],'feature3':[],'feature4':[],
                   'feature5':[],'feature6':[],'feature7':[],'feature8':[],
                   'feature9':[]}
    truth = []
    #log
    logger = get_logger(__name__)                  
    logger.info("*" * 20 + "invoke" +  "*" * 20)
    #config
    model_config = ConfigParser()               
    model_config.optionxform = str
    model_config.read("../config/model_configure.ini")
    max_depth_d = model_config.get('model_par', 'max_depth') 
    max_leaf_nodes_d = model_config.get('model_par', 'max_leaf_nodes') 

    #input
    features,truth = input_coal_data(features_dict)

    x_test_data,x_train_data,y_train_data,y_test_data = divide_data(features,truth)

    x_test_data_pca,x_train_data_pca,pca = pca_model(x_test_data,x_train_data)

    features_dict = input_raw_data(features_dict)

    x_test_data_raw,x_train_data_raw = divide_raw_data(features_dict)

    x_test_all,x_train_all = add_features(x_test_data_pca,x_train_data_pca,x_test_data_raw,x_train_data_raw)

    print("[data_process]: done")

    tree = tree_model(x_train_all, y_train_data,int(max_depth_d),int(max_leaf_nodes_d))

    test_val(tree,x_test_all,x_train_all,y_test_data,y_train_data)

    print("[model_process]: done")

    #save model
    joblib.dump(pca, '../models/vdaf_pca.pkl')
    joblib.dump(tree, '../models/vdaf_tree.pkl')
    logger.info(tree)
    print("[save model]: done")