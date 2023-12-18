import logging
import logging.config
import os
from os.path import dirname, abspath  

def get_logger(name: str = "root"):
    parent_dir = dirname(dirname(abspath(__file__)))
    if not os.path.exists(parent_dir + "/logs/prediction.log.2022-6-19"):
        file = open(parent_dir + "/logs/prediction.log", "w+")
        file.close()
    conf_log = abspath(parent_dir + "/config/log.conf")
    logging.config.fileConfig(conf_log)
    return logging.getLogger(name)

if __name__ == "__main__":
    get_logger(__name__)