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

#which one to use ?
# Insertion Sort should be used with only a few items if your input is small or items are mostly sorted.
# Bubble Sort is only used for educational purposes as a way to teach sorting, but its very rare to find this in real life because it is not efficient
# Selection Sort is the time, it is not used mostly.
# Merge Sort is really, really good because of divide and conquer we have O(nlogn), it is fast. In all cases it is the same.
#   if we are worried about the worst case, we should use Merge Sort.
#   However, it uses O(n) space complexity. If there is not a lot of space in memory. We should reconsider using merge sort
# Quick Sort's space complexity's O(logN) with time complexity O(nlogn), but its worst case O(n^2)
# Heap Sort is slower than Quick Sort in most cases https://brilliant.org/wiki/heap-sort/
# Mathematically O(n logn) cannot be beatable if we use comparison.
# The sorting algorithms above are Comparison Sort
# Counting Sort, Radix Sort are Non-Comparison Sort. which let us to sort using bit and bytes but it works only with specially integers.
# Radix Sort: https://brilliant.org/wiki/radix-sort/
# Radix Sort Animation: https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
# Counting Sort: https://brilliant.org/wiki/counting-sort/
# Counting Sort Animation: https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

# Python built-in sort method:
#Python uses an algorithm called Timsort:
#Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. 

# in js it differs with browsers
# V8 in chrome uses quick sort and insertion sort

# https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link