#when it comes to small data, it is okay to use built-in methods that comes with the programing language we use.
#However, when it is big data, it is really hard to access the data when it is not sorted. 
# big companies uses custom sorting methods to sort data, and they need you to understand how it works to lower their cost of the company

# the issue of the built-in methods
#https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
#https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare

basket = [2,65,34,2,1,7,8]
basket.sort()
print(basket)

#in javascript, built in function of sort, sorts the data wrongly. It first converts to number to string than compare its unicode
#https://www.toptal.com/developers/sorting-algorithms