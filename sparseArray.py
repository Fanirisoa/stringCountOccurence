#! /usr/bin/python/  python3
# coding: utf-8

class setStringToCompare:
    """
    A class used to represent a collection of query strings and a collection of input strings

    ...

    Attributes
    ----------
    queries : array[str]
        an array of query strings
    strings : array[str]
       an array of strings to search

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

	# définition de la méthode spéciale __init__
    def __init__(self, queries, strings):
        """
        a constructor to initialize the attributes of the class setStringToCompare.

        : queries : array[str]  an array of query strings
        : strings : array[str]  an array of strings to search
        """
        self.queries = queries
        self.strings = strings


    
    def matchingStringsToVec(self):
       """ 
       Customize function matchingStringsToVec : Compare queries and strings and return  an integer array of occurence.
        
        : param e : the column
        : return  : an array of integers representing the frequency of occurrence of each query string in strings.
       """
        countList = []
        for _ in self.queries:
            countList.append(self.strings.count(_))
        return countList   

    def matchingStringsToDic(self):
       """ 
       Customize function matchingStringsToDic : Compare queries and strings and return a dictionary of occurence where 
            - key[i] : queries[i]  ith element of queries
            - value[i] : the frequency of occurrence of queries[i] in strings
        
        : param e : the column
        : return  : an array of integers representing the frequency of occurrence of each query string in strings.
       """    
        return dict((x,self.strings.count(x)) for x in set(self.queries))


dataUsed = setStringToCompare(['blue', 'red',  'yellow','green'],['blue', 'red', 'blue', 'yellow', 'blue', 'red', 'yellow', 'blue', 'red', 'red', 'blue'])




print(dataUsed.matchingStringsToVec())
print(dataUsed.matchingStringsToDic())

