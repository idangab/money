import random
class BaseStrategy(object):
    def __init__(self, envelope):
        self.envelope = envelope
        self.counter=0

    def display(self):
        count=""
        for self.counter in range(len(self.envelope)):
            count+= str(self.envelope[self.counter].money) + ", "
        return count

    def perform_strategy(self, counter):
        for i in range(len(self.envelope)):
            if i == 69:
                self.envelope[i].used =True
                print( "The money from the envelope: " + str(self.envelope[i].money))
            else:
                self.envelope[i].used = True


    def play(self):
        self.perform_strategy(8)

class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelope):
        BaseStrategy.__init__(self, envelope)

    def perform_strategy(self, counter):
        rnd= random.randrange(100)
        for i in range(len(self.envelope)):
            if i == rnd:
                self.envelope[i].used =True
                print( "The money from the envelope: " + str(self.envelope[i].money))
            else:
                self.envelope[i].used = True

class N_max_strategy(BaseStrategy):
    def __init__(self, Envelope):
        self.N=3
        BaseStrategy.__init__(self, Envelope)

    def perform_strategy(self, counter):
        arr= []
        arr1= []
        for i in range(len(self.envelope)):
           if(i< self.N):
               arr.append(self.envelope[i].money)
               self.envelope[i].used= True
           else:
               arr1.append(self.envelope[i].money)
               self.envelope[i].used = True
        arr.sort()
        print("max of 10% is "+ arr[-1])
        arr1.sort()
        if(arr[-1] > arr1[-1]):
            print("The money from the envelope (from percentage): " + str(arr[-1]))
        if (arr[-1] < arr1[-1]):
            print("The money from the envelope (from the leftovers): " + str(arr1[-1]))
        else:
            print("The money from the (they are equals in both parts): " + str(arr1[-1]))





class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, Envelope, a):
        self.percent = a
        BaseStrategy.__init__(self, Envelope)

    def perform_strategy(self, counter):
        arr= []
        for i in range(len(self.envelope)):
           arr.append(self.envelope[i].money)
        max=arr[0]
        for i in range(len(arr)):
            if (int(self.percent) - 1 != 0):
                if (arr[i] > max):
                    max= arr[i]
                    (self.percent)= int(self.percent)-1
            else:
                break
        print("The money from the N maximal envelope: " + str(max))

