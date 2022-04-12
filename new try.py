import requests
from bs4 import BeautifulSoup as bs
from price_printing import price_print
from website_search_extractor import extractor 
from price_printing import price_print
#1 is for amazon
#2 if for flipkart
amazon="https://www.amazon.in/s?k="
flipkart="https://www.flipkart.com/search?q="
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"} #give the information about the software dealing with web scripts 
#creating the link for searching across the sites
product=(input("Enter the  product name to serach:-"))
product_name=product.replace(' ','+')

amazon_search=amazon+product_name

flipkart_search=flipkart+product_name

search_results_1=[]
search_results_2=[]

a=extractor(amazon_search,flipkart_search,headers)

search_results_1=a[0]

search_results_2=a[1]

print(search_results_1)
print(search_results_2)
new_search_results_1=[]
t=[]
price_print()
# for q in (str(search_results_1)):
    # for i in range(len(q)):
        # for e in range(len(product)):
            # t=t+q[i]
        # new_search_results_1.append(t)
# print(new_search_results_1)
