#! /usr/bin/python/  python3
# coding: utf-8

class setStringToCompare:


	# définition de la méthode spéciale __init__
    def __init__(self, queries, strings):
        # deux paramètres supplémentaires
        self.queries = queries
        self.strings = strings


    # matchingStringsToVec function: Compare queries and strings and return a vector of occurence.
    def matchingStringsToVec(self):
        countList = []
        for _ in self.queries:
            countList.append(self.strings.count(_))
        return countList   

    # matchingStringsToDic function: Compare queries and strings and return a vector of occurence.
    def matchingStringsToDic(self):    
        return dict((x,self.strings.count(x)) for x in set(self.queries))


dataUsed = setStringToCompare(['blue', 'red',  'yellow','green'],['blue', 'red', 'blue', 'yellow', 'blue', 'red', 'yellow', 'blue', 'red', 'red', 'blue'])




print(dataUsed.matchingStringsToVec())
print(dataUsed.matchingStringsToDic())

