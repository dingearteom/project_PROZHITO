from pullenti_client import Client
from slovnet.span import Span
import copy
import docker
import os

class Dates:
    def __init__(self):
        self.client = Client('localhost', 8083)

    def fit(self, document):
        result = self.client(document)
        dates = []

        for match in result.matches:
            if (match.referent.label == 'DATE'):
                try:
                    dates.append(Date(match.referent, match.span))
                except:
                    pass
            elif (match.referent.label == 'DATERANGE'):
                try:
                    dates.append(DateRange(match.referent, match.span))
                except:
                    pass
            else:
                raise NameError('Unknown time entity type.')
        return dates


class Date:
    def __init__(self, date, span):
        self.span = span
        self.day = None
        self.month = None
        self.year = None
        m = {'DAY': 'day', 'MONTH': 'month', 'YEAR': 'year'}

        def get_date(object, date_):
            for slot in date_.slots:
                if (slot.key in ['DAY', 'MONTH', 'YEAR']):
                    Date.__setattr__(object, m[slot.key], int(slot.value))
                elif (slot.key == 'HIGHER'):
                    get_date(object, slot.value)
                else:
                    pass
            return
        get_date(self, date)
    def to_num(self):
        return (0 if self.day is None else 1) + \
               ((0 if self.month is None else 1) << 1) + \
               ((0 if self.year is None else 1) << 2)

    def encode(self):     ## json encoder
        res = copy.deepcopy(self.__dict__)
        res['type'] = 'Date'
        res['span'] = res['span'].__dict__
        return res

    def __str__(self):
        return (("Day:" + str(self.day)) if (not self.day is None) else "") \
               + (" Month:" + str(self.month) if (not self.month is None) else "") \
               + (" Year:" + str(self.year) if (not self.year is None) else "")

class DateRange:
    def __init__(self, date, span):
        self.span = span
        self.start = None
        self.stop = None
        for slot in date.slots:
            if (slot.key == 'FROM'):
                self.start = Date(slot.value, Span(0, 0))
            elif (slot.key == 'TO'):
                self.stop = Date(slot.value, Span(0, 0))

    def encode(self):
        res = copy.deepcopy(self.__dict__)
        res['type'] = 'DateRange'
        res['span'] = res['span'].__dict__
        if (not res['start'] is None):
            res['start'] = res['start'].encode()
        if (not res['stop'] is None):
            res['stop'] = res['stop'].encode()
        return res
    def to_num(self):
        return (1 << 6) + \
               ((self.start.to_num() if (not self.start is None) else 0) << 3) + \
               (self.stop.to_num() if (not self.stop is None) else 0)


    def __str__(self):
        return "From " + self.start.__str__() + " To " + self.stop.__str__() + "\n"
