'''
from us_visa.logger import logging
from us_visa.exception import USvisaException

import sys

#logging.info("It is running")
try:
    a = 1 /"10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e    
'''





from us_visa.pipeline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()
'''

from us_visa.constant import *
print(DATA_INGESTION_DIR_NAME)

''' 