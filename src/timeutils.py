'''
Created on Apr 9, 2012

@author: peng
'''
import datetime

_EPOCH = datetime.datetime(1970, 1, 1)


def utc_timestamp(value=None):
    '''get utc timestamp'''
    if not value:
        value = datetime.datetime.utcnow()
    td = value - _EPOCH
    ts = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6
    return int(ts)


def get_last_week(value=None):
    '''get one week's date'''
    if not value:
        value = datetime.datetime.now()
    week_num = value.weekday()

    end_date = value - datetime.timedelta(days=week_num)
    days = 7
    week_days = []
    while days:
        end_date -= datetime.timedelta(days=1)
        week_days.append(end_date)
        days -= 1
    return week_days
