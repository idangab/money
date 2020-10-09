import random
class BaseStrategy(object):
    def __init__(self, envelope):
        self.envelope = envelope
        self.counter=0

    def display(self):
        sentence = ""
        for self.counter in range(len(self.envelope)):
            sentence += str(self.envelope[self.counter].money) + ", "
        return sentence

    def play(self):
        self.perform_strategy(8)


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelope):
        BaseStrategy.__init__(self, envelope)


class N_max_strategy(BaseStrategy):
    def __init__(self, Envelope):
        self.N=3
        BaseStrategy.__init__(self, Envelope)


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, Envelope, a):
        self.percent = a
        BaseStrategy.__init__(self, Envelope)

