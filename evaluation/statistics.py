def evaluate(right_spans, spans):
    j = 0

    missed = 0
    error = 0
    right = 0
    for i in range(len(right_spans)):
        while (j < (len(spans)) and spans[j].start < right_spans[i].start):
            j += 1
            error += 1
        if (j < len(spans) and spans[j] == right_spans[i]):
            right += 1
            j += 1
        else:
            missed += 1
    error += (len(spans) - j)
    total = missed + right
    return statistics(len(right_spans), len(spans), missed, error)

class statistics:
    __attributes__ = ['total_true', 'total_answered', 'missed', 'error']
    total_true = total_answered = _missed = _error = right = missed_rate = error_rate = right_rate = 0

    def __init__(self, *args, **kwargs):
        for key, value in zip(self.__attributes__, args):
            self.__setattr__(key, value)
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    @property
    def missed(self):
        return self._missed
    @missed.setter
    def missed(self, value):
        self._missed = value
        self.missed_rate = (self._missed / self.total_true) * 100

    @property
    def error(self):
        return self._error
    @error.setter
    def error(self, value):
        self._error = value
        self.right = self.total_answered - self._error
        self.error_rate = (self._error / self.total_answered) * 100
        self.right_rate = (self.right / self.total_answered) * 100
    def __add__(self, other):
        return statistics(self.total_true + other.total_true, self.total_answered + other.total_answered, self.missed + other.missed, self.error + other.error)

    def __str__(self):
        s = f"Total in the documents: {self.total_true}\nTotal answered by model: {self.total_answered}\n"
        s += f"missed_rate: {self.missed_rate}%\nerror_rate: {self.error_rate}%\nright_rate: {self.right_rate}%"
        return s

