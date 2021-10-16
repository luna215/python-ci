from configparser import Error
import os
import logging.config
import traceback
import time


print('Trying to increase the complexity of this file')
# class CustomAdapter(logging.LoggerAdapter):
#     def process(self, msg, kwargs):
#         my_context = kwargs.pop('slide', self.extra['slide'])
#         return '[%s] %s' % (my_context, msg), kwargs

class DatabookFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log
    """
    REQUEST_ID = 123
    ENVIRONMENT = 'production'
    COMPANY = 'Databook'
    ORGANIZATION = 'Accenture'

    #... Among other things

    def filter(self, record):

        record.request_id = DatabookFilter.REQUEST_ID
        record.environment = DatabookFilter.ENVIRONMENT
        record.company = DatabookFilter.COMPANY
        record.organization = DatabookFilter.ORGANIZATION

        return True

logging.config.fileConfig(os.path.abspath('logging.ini'), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# logger = CustomAdapter(logger, {'slide': None})

databook_filter = DatabookFilter()
logger.addFilter(databook_filter)


def record_word_count(myfile):
    for i in range(10000):
        starttime = time.time()
        try:
            raise ValueError('There was an issue')
        except:

            endtime = time.time()
            duration = endtime - starttime
            logger.error("Deckbot crashed: %s", traceback.format_exc(), extra={'run_duration': duration, "request_id": 123, 'user_email': 'paul.luna+salesforce@trydatabook.com'})
            logger.error("Deckbot crashed: %s", traceback.format_exc())
    
    raise Error("Exiting app")

if __name__ == '__main__':
    try:
        record_word_count('doesnotexist.txt')
    except:
        logger.error("Deck didn't finish correctly %s", traceback.format_exc())