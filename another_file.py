from configparser import Error
import os
import logging.config
import traceback
import time

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('slide', self.extra['slide'])
        return '[%s] %s' % (my_context, msg), kwargs

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {'slide': None})

def record_word_count(myfile):
    for i in range(100000):
        starttime = time.time()
        try:
            raise ValueError('There was an issue')
        except:
            endtime = time.time()
            duration = endtime - starttime
            logger.error("Deckbot crashed: %s", traceback.format_exc(), slide='ExecutiveSummary', extra={'run_duration': duration, "request_id": 123, "organization": "salesforce", 'targat_company': 456, 'user_id': 321, 'user_email': 'paul.luna+salesforce@trydatabook.com'})
            logger.error("Deckbot crashed: %s", traceback.format_exc(), slide='SolutionsSlide')
    
    raise Error("Exiting app")

if __name__ == '__main__':
    try:
        record_word_count('doesnotexist.txt')
    except:
        logger.error("Deck didn't finish correctly %s", traceback.format_exc())