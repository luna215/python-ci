import os
import logging.config
import traceback
import time

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def record_word_count(myfile):
    for i in range(100000):
        logger.error("starting the function")
    
    raise ValueError

if __name__ == '__main__':
    try:
        starttime = time.time()
        record_word_count('doesnotexist.txt')
    except:
        endtime = time.time()
        duration = endtime - starttime
        logger.error("uncaught exception: %s", traceback.format_exc(), extra={'run_duration': duration})
        print('there was an error')