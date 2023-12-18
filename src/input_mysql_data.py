
import pymysql
import numpy as np

def input_mysql_data(features_dict,truth):
    mysql_conn = pymysql.connect(host = 'xx.xxx.xx.xxx', port = 'xxxxx', user = 'xxxx', password = 'xxxxxxxxx', db = 'xxxxx')
    cursor = mysql_conn.cursor()
    
    for c0 in range(439):  
        xsql = "SELECT C8 FROM 23_1_out_out WHERE C0='" + str(c0) + "'"
        cursor.execute(xsql)
        xresults = cursor.fetchall()  

        for feature in features_dict:
            i = 0
            features_dict[feature] = np.mat(features_dict[feature].append(float(xresults[i][0])))
            i += 1

        ysql = "SELECT C6 FROM 23_1_y WHERE C0='" + str(c0) + "'"
        cursor.execute(ysql) 
        yresults = cursor.fetchall()  
        truth.append(float(yresults[0][0]))
        res1 = cursor.execute(xsql)   
        res2 = cursor.execute(ysql)
        print(res1, res2)

    mysql_conn.close()
    return features_dict, truth