"""
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean of all temps we've seen so far
get_mode()—returns the mode of all temps we've seen so far
Optimize for space and time.

Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can return integers.

Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.

If there is more than one mode, return any of the modes.

"""

#TODO: make this O(1) space and time

class TempTracker(object):

    def __init__(self):
        self.temps = []
        self.counts = {}
        self.max = None
        self.min = None

    def insert(self, temp):
        """records new temp (int)"""
        self.temps.append(temp)
        # if this is first temperature we've seen, its also max & min
        if not self.temps:
            self.max = temp
            self.min = temp
        else:
            self.max = max(self.max, temp)
            self.min = min(self.min, temp)

        counts[temp] = counts.get(temp, 0) + 1

    def get_max(self):
        """returns the highest temp we've seen so far"""
        return self.max

    def get_min(self):
        """returns the lowest temp we've seen so far """
        return self.min

    def get_mean(self):
        """returns the mean of all temps we've seen so far as a float """
        return float(sum(self.temps))/float(len(self.temps))

    def get_mode(self):
        """returns the mode of all temps we've seen so far
        the number which appears the most times
        if more than one num, returns lowest
        """
        pass
