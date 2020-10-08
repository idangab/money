def perform_strategy(counter, envelope): #strategy4
    arr = []
    for i in range(len(envelope)):
        arr.append(envelope[i].money)
    max = arr[0]
    for i in range(len(arr)):
        if (int(percent) - 1 != 0):
            if (arr[i] > max):
                max = arr[i]
                (percent) = int(percent) - 1
        else:
            break
    print("The money from the N maximal envelope: " + str(max))