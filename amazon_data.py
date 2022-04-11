from os import name
from bs4 import BeautifulSoup as bs
import dictionary_maker as dic

def amazon_name(file_name):
    #this file is opened for names
    file=open('amazon_data.html','r',encoding="utf-8")
    contents=file.read()

    to_search=bs(contents,'lxml')
    to_search.prettify()

    name_list=[]
    
    #fetching the name
    b=to_search.find_all('span',class_="a-size-medium a-color-base a-text-normal")
    print(len(b))
    for i in range(5):
        c=str(b[i])
        d=c.strip('<span class="a-size-medium a-color-base a-text-normal"></span>')
        name_list.append(d)
        #print(d)
    print(name_list)
    return(name_list)


def amazon_price(price_file):

    #this file is opened is for price
    prices=open('amazon_data.html','r',encoding="utf-8")
    price_contents=prices.read()

    search_price=bs(price_contents,'lxml')
    search_price.prettify()

    #print(b)
    
    f=[]

    #fetchignt the price
    b=search_price.find_all('span',class_="a-price-whole")
    for i in range(5):
        c=str(b[i])
        d=c.strip('<span class="a-price-whole"></span>')
        #if d.find('<span class="a-price-decimal">')==True:
        #    print('found')
        #    pass
        #else:
        f.append(d)
    print(len(f))

    return(f)

#this function saves images of the selected product

#to complete this feature at the end 
