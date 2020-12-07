import pandas as pd
from model.Dates.dates import Dates
from scipy.spatial.distance import euclidean

class Type_of_Text:
    def __init__(self):
        pass
    def fit(self, document):
        model_time = Dates()
        dates = model_time.fit(document)
        arr = [0 for i in range(1 << 7)]
        for date in dates:
            arr[date.to_num()] += 1
        for i in range(1 << 7):
            arr[i] /= len(dates)
        t = pd.Series(arr)
        t = t.sort_values()
        threshold = 0.2
        if (t[7] + t[3] >= threshold):
            return 'Diary'
        else:
            return 'Memoir'


