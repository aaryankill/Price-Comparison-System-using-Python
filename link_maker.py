from os import name
from bs4 import BeautifulSoup as bs
from amazon_data import amazon_name
import dictionary_maker as dic
from prodcut_page_data import flipkart_data

#function for making the links for searching across the sites
def links(name):
    name_1=str(name)
    replaced_name=name_1.replace(' ','+')
    amazon="https://www.amazon.in/s?k="
    flipkart="https://www.flipkart.com/search?q="
    amazon_link=amazon+replaced_name
    flipkart_link=flipkart+replaced_name
    return(amazon_link,flipkart_link)

#getting the product page URL for the selected product from amazon
def amazon_product_link(product_name):
    file=open('amazon_data.html','r',encoding="utf-8")
    contents=file.read()
    
    file_content=bs(contents,'lxml')
    file_content.prettify()
    
    #saving the tags conatianing the links 
    all_links=file_content.find_all('a',class_="a-link-normal s-link-style a-text-normal",target='_blank',href=True)
    names_list=amazon_name('doesnt matter')
    print(len(names_list))
    
    #getting the product links stored in a list
    links_list=[]
    c0=0
    for link in all_links:
        links=link.get('href')
        amazon='https://www.amazon.in'
        link_1=amazon+links
        links_list.append(link_1)
        c0+=1
        if c0==5:
            break

    print(len(links_list))

    #made a dictionary with product names with their correspoding links 
    dictionary=dic.dic_maker(names_list,links_list)

    #comparing the names to get so that the required link is returned
    for i in names_list:
        if (product_name==i):
            print(dictionary[product_name])
            return(dictionary[product_name])



#getting the product page for the selected product from flipkart
def flipkart_product_link(product_name):
    file=open('flipkart_data.html','r',encoding="utf-8")
    contents=file.read()
    
    file_content=bs(contents,'lxml')
    file_content.prettify()

    #saving the tags conatianing the links 
    all_links=file_content.find_all('a',class_="_1fQZEK",target="_blank",rel="noopener noreferrer",href=True)
    
    #getting the product links stored in a list    
    links_list=[]
    for link in all_links:
        links=link.get('href')
        flipkart='https://www.flipkart.com'
        link_1=flipkart+links
        links_list.append(link_1)
    names=file_content.find_all('div',class_="_4rR01T")
    
    #making a list for storing all the names
    name_list=[]
    for name_tag in names:
        i=str(name_tag)
        name=i.strip('<div class="_4rR01T> </div>')
        name_list.append(name)

    #made a dictionary with product names with their correspoding links
    dictionary=dic.dic_maker(name_list,links_list)
    for i in name_list:
        if (product_name==i):
            print(dictionary[product_name])
            return(dictionary[product_name])