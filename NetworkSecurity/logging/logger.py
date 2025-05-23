import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## This How my LOG FILE will Look Like 

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)  ## The path of the Logs are created i.e 'logs' Folder will be created inside that LOG_FILE will get created 

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)  ## This is the Location of the LOG_FILE path 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)