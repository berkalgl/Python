#https://www.bigocheatsheet.com
#1 - Sort 10 schools around your house by distance:
# Insertion Sort space complexity O(1)

#2 - eBay sorts listings by the current Bid amount:
# Radix or Counting Sort, one dollar to 50 dollars, fixed length of integer, to beat O(nlogn)

#3 - Sport scores on ESPN
# Quick Sort, we are worried about space complexity

#4 - Massive database (can't fit all into memory) needs to sort through past year's user data
# Merge Sort , we are not really sorting in memory because the data is so big, i am really worried about performance to avoid Quick Sort worst
# case of O(n^2)

#5 - Almost sorted Udemy review data needs to update and add 2 new reviews
# Insertion Sort, although this data might be huge, but it is already sorted. Intertion works highly better than any other algorithm

#6 - Temperature Records for the past 50 years in Canada
# if the temperatures have no decimal places --> radix, counting sort
# if not, quick sort, memory sorting

#7 - Large user name database needs to be sorted. Data is very random.
# Merge Sort if we have enough memory. but if we are not too worried about the worst case, we can use Quick Sort

#8 - You want to teach sorting for the first time
# Bubble Sort, Selection Sort