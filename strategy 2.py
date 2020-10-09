def perform_strategy(self, counter, envelope):
        rnd= random.randrange(100)
        for i in range(len(envelope)):
            if i == rnd:
                envelope[i].used =True
                print( "The money from the envelope: " + str(envelope[i].money))
            else:
                envelope[i].used = True