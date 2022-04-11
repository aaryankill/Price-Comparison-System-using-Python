from os import name
from bs4 import BeautifulSoup as bs

def data_for_flipkart(file_name):
    file=open(file_name,'r',encoding="utf-8")
    contents=file.read()
    
    to_search=bs(contents,'lxml')
    to_search.prettify()
    
    #fetching the name
    b=to_search.find_all('div',class_="_4rR01T")
    e=[]
    for i in range(5):
        c=str(b[i])
        d=c.strip('div class_="_4rR01T">  </div>')
        e.append(d)

    #fetching the price
    b=to_search.find_all('div',class_="_30jeq3 _1_WHN1")
    f=[]
    for i in range(5):
        c=str(b[i])
        d=c.strip('<div class_="_30jeq3 _1_WHN1>')
        #print(d)
        f.append(d)
    #had to do this cause the 'strip' was not able to removce the closing div tag
    v=[]
    for i in f:
        c=i[:-2]
        v.append(c)
    
    #saving the data in form of a dictionary
    name_and_price={}
    
    for i in range(len(e)):
        name_and_price[(e[i])]=v[i]
    #print(name_and_price)
    return(name_and_price)