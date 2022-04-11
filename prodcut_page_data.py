import requests
from bs4 import BeautifulSoup as bs
from requests.api import delete
from requests.models import ReadTimeoutError


def amazon_data(product_link):
    product_link_1=product_link+'.txt'
    #headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"} #give the information about the software dealing with web scripts 
    headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    #getting the data from the product page
    a=requests.get(product_link_1,headers=headers)
    b=a.text
    data=bs(b,'lxml')
    data.prettify()
    print(len(data))


    #fetching all the basic details about the product from the product page
    
    #name
    name=data.find_all('span',id="productTitle",class_="a-size-large product-title-word-break") 
    name_1=str(name)
    print(name_1)
    name_2=name_1.strip('<span id="productTitle" class="a-size-large product-title-word-break"> </span>')
    print(name_2)

    #price
    price=data.find('span',class_="a-offscreen")
    price_1=str(price)
    price_2=price_1.strip('<span class="a-offscreen"> </span>')
    print(price_2)

    #rating
    rating=data.find('span',class_="a-icon-alt")
    rating_1=str(rating)
    rating_2=rating_1.strip('<span class="a-icon-alt"> </span>')
    print(rating_2)

    #about the item
    details=data.find('ul',class_="a-unordered-list a-vertical a-spacing-mini")
    print(len(details))
    details_3=[]
    for i in details:
        i_1=str(i)
        details_1=i_1.strip('<li><span class="a-list-item">')
        details_2=details_1.strip('</span></li>')
        details_3.append(details_2)
    for i in details_3:
        if (i==''):
            details_3.remove(i)
    print(details_3)
    
    #saving the image of the product

    return(name_2,price_2,rating_2,details_3)



def flipkart_data(product_link):
    #headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"} #give the information about the software dealing with web scripts 
    headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    #getting the data from the product page
    a=requests.get(product_link,headers=headers)
    b=a.text
    data=bs(b,'lxml')
    data.prettify()

    #fetching all the basic details about the product from the product page
    
    #name
    name=data.find('span',class_="B_NuCI")
    name_1=str(name)
    name_2=name_1.strip('<span class="B_NuCI"></span>')
    
    #price
    price=data.find('div',class_="_30jeq3 _16Jk6d")
    price_1=str(price)
    price_2=price_1.strip('<div class="_30jeq3 _16Jk6d">')
    price_3=price_2.replace('</div>','')
    price_4=price_3[:-2]

    #rating
    rating=data.find('div',class_="_3LWZlK")
    rating_1=list(rating)

    #about the item
    details=data.find_all('li',class_="_21Ahn-" )

    details_1=[]
    
    for i in details:
        i_1=str(i)
        i_2=i_1.strip('<li class="_21Ahn-"></li>')
        details_1.append(i_2)


    return(name_2,price_4,rating_1[0],details_1)