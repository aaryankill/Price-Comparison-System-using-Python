#dictionary maker
from os import name


def dic_maker(key,value):
    dictionary={}
    cou=0 #it is a counter
    #adding the name and price of the product in the dictionary
    for names in key:
        dictionary[names]=value[cou]
        cou+=1
    return (dictionary)