from sklearn.tree import DecisionTreeRegressor
import numpy as np

def tree_model(x_train_data, y_train_data,max_depth_d,max_leaf_nodes_d):
    tree = DecisionTreeRegressor(max_depth = max_depth_d,max_leaf_nodes = max_leaf_nodes_d)
    tree.fit(x_train_data, y_train_data)
    return tree

