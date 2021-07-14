import logging
from pytz import timezone
from _datetime import datetime

timeZone = timezone('EST')
startLog = logging.getLogger()
occurenceInfo = datetime.now(timeZone)
def updateLog(phrase):
    startLog.info("On " + str(occurenceInfo) + ": " + phrase)
    return 0