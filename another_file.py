
import os
from os import path

import logging.config

import main

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

os.system('pwd')

def record_word_count(myfile):
    logger.info("starting the function")
    try:
        word_count = main.word_count(myfile)
        with open('wordcountarchive.csv', 'a') as file:
            row = str(myfile) + ',' + str(word_count)
            file.write(row + '\n')
    except:
        logger.warning("could not write file %s to destination", myfile)
    finally:
        logger.debug("the function is done for the file %s", myfile)


if __name__ == '__main__':
    record_word_count('doesnotexist.txt')
    os.system('cat file.log')
    










