import os
import logging.config
import traceback
import time

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def word_count(myfile):
    try:
        # count the number of words in a file, myfile, and log the result
        starttime = time.time()
        with open(myfile, 'r+') as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            endtime = time.time()
            duration = endtime - starttime
            starttime = time.time()
            logger.info("this file has %d words", final_word_count, extra={"run_duration":duration})
            return final_word_count
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False

if __name__ == '__main__':
    word_count('myfile.txt')

    