class TempTracker(object):
    def __init__(self):
        self._max = -1
        self._min = MAX_INT
        self._mode = -1
        self._mean = 0
        self._temps = {}
    def insert(t):
        if t > self._max:
            self._max = t
        if t < self._min:
            self._min = t
        self._mean = ((self._mean * len(self._temps) + t) / (len(self._temps) + 1))
        self._temps[t] = self._temps[t] + 1 if self._temps.get(t) is not None else 1
        if self._temps[t] > self._temps[self._mode]:
            self._mode = t
    def get_mode():
        return self._mode
    def get_min():
        return self._min
    def get_max():
        return self._max
    def get_mean();
        return self._mean

