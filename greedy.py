class LuggageItem(object):
    def __init__(self, weight, priority, isFractionable):
        self.weight = weight
        self.priority = priority
        self.isFractionable = isFractionable

    def __lt__(self, other): 
        return self.priority < other.priority


def processGreedy(W, P, ISFRAC, n, weightLimit):
    luggage = []
    remaingWeight = weightLimit
    totalWeight = 0
    generator = range(n)

    for i in generator: 
        luggage.append(LuggageItem(W[i], P[i], ISFRAC[i]))            

    luggage.sort(reverse = True)

    for i in generator:
        tempItem = luggage[i] 
        if(tempItem.weight <= remaingWeight):
            remaingWeight -= tempItem.weight
            totalWeight += tempItem.weight
            print("Item: {}, Weight {}, Priority {}".format(i, tempItem.weight, tempItem.priority))

        elif(tempItem.isFractionable):
            totalWeight += remaingWeight
            print("Item: {}, Original Weight {}, Fractioned Weight {}, Priority {}".format(i, tempItem.weight, remaingWeight, tempItem.priority))
            remaingWeight = 0

        if (totalWeight == weightLimit):
            break

    print("Total weight: {}".format(totalWeight))


WEIGHTS = [15, 18, 2, 4] 
PRIORITIES = [0, 25, 2, 6]
ISFRAC = [1, 1, 0, 1]
totalItems = 4
weightLimit = 20

processGreedy(WEIGHTS, PRIORITIES, ISFRAC, totalItems, weightLimit)