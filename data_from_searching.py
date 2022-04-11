#saving all the data in a text file
import requests
from bs4 import BeautifulSoup as bs
from requests.api import head
def text_save(site_url_1,site_url_2):
    
    #saving data of amazon
    #headers={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"} #give the information about the software dealing with web scripts 
    headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    a=requests.get(site_url_1,headers=headers)
    b=bs(a.content,'lxml')
    b.prettify()
    c=b.find_all('div',class_="s-include-content-margin s-latency-cf-section s-border-bottom s-border-top")
    file=open('amazon_data.html','w',encoding="utf-8")
    file.writelines(str(c))

    #in amazon,for prices I had to make another file and save the price in them
    c=b.find_all('span' , class_="a-price-whole")
    price=open('amazon_price.html','w')
    price.writelines(str(c))

    #saving data of flipkart
    a=requests.get(site_url_2,headers=headers)
    b=bs(a.content,'lxml')
    b.prettify()
    c=b.find_all('a',class_="_1fQZEK",target="_blank",rel="noopener noreferrer",href=True)
    file=open('flipkart_data.html','w',encoding="utf-8")
    file.writelines(str(c))    