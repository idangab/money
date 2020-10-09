def perform_strategy(counter, envelope, N):
        arr= []
        arr1= []
        for i in range(len(envelope)):
           if(i< N):
               arr.append(envelope[i].money)
               envelope[i].used= True
           else:
               arr1.append(envelope[i].money)
               envelope[i].used = True
        arr.sort()
        print("max of 10% is "+ arr[-1])
        arr1.sort()
        if(arr[-1] > arr1[-1]):
            print("The money from the envelope (from percentage): " + str(arr[-1]))
        if (arr[-1] < arr1[-1]):
            print("The money from the envelope (from the leftovers): " + str(arr1[-1]))
        else:
            print("The money from the (they are equals in both parts): " + str(arr1[-1]))