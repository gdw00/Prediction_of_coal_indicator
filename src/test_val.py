

def test_val(tree,x_test_data,x_train_data,y_test_data,y_train_data):
    prediction = tree.predict(x_test_data)
    #training set
    print("max_leaf_nodes=2,min_samples_leaf = 2")
    error = 0
    every_error = []
    yt1 = tree.predict(x_train_data)   
    for i in range(351):
        loss1 = abs(yt1[i]-y_train_data[i])
        error = error + loss1
        every_error.append(loss1[0])
    ans1 = error/352
    print("Average error of training set:",ans1)
    print("Error",every_error)
    #Test set
    every_error = []
    error = 0
    for i in range(87):
        loss2 = abs(prediction[i]-y_test_data[i])
        error = error + loss2
        every_error.append(loss2[0])
    ans2 = error/87
    print("Average error of tset set:",ans2)
    print("Error",every_error)
