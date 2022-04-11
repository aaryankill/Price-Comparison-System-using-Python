import matplotlib.pyplot as mp

def price_comparison(amazon_data,flipkart_data):
    
    #seperating the data of the amazon product
    a_name=amazon_data[0]
    a_price=int(amazon_data[1])
    a_rating=amazon_data[2]
    a_details=amazon_data[3]

    #seperating the data for flipkart product
    f_name=flipkart_data[0]
    f_price=int(flipkart_data[1])
    f_rating=flipkart_data[2]
    f_details=flipkart_data[3]

    #differnece between the price
    if a_price>f_price:
        difference_in_prices=a_price-f_price
    else:
        difference_in_prices=f_price-a_price
    
    

    x_axis=[0,1,2]
    #x_axis.append(a_name)
    #x_axis.append(f_name)
    y_axis=[b_var]
    y_axis.append(a_price)
    y_axis.append(f_price)

    mp.bar(x_axis,y_axis)
    mp.show()