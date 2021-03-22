import os
import logging.config
import traceback
import time

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def record_word_count(myfile):
    for i in range(100000):
        starttime = time.time()
        try:
            raise ValueError('There was an issue')
        except:
            endtime = time.time()
            duration = endtime - starttime
            logger.error("uncaught exception: %s", traceback.format_exc(), extra={'run_duration': duration})
    
    raise ValueError

if __name__ == '__main__':
    try:
        record_word_count('doesnotexist.txt')
    except:
        logger.error("Deck didn't finish correctly")