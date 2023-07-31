# Sorting-algorithms-training
A simple code where write famous sorting algorithms, from simple ones to more complex ones. 
Done purely for education and study purposes. 
Includes a time measurement to compare the speed of each one.

The lists are entirely composed of integers and are always sorted in ascending order.
The program provides the user with the following small premade list: [3,7,8,8,4,2,6,1], which can be replaced by customizable one by the user.

# Libraries used
*random (randInt() function)
Used randInt for generating lists composed of random integers to test in te different sorting algorithms

*time (time() function)
Used for timing the duration of each sorting algorithm

# Bubble sort
The simplest sorting algorithm. It iterates over the unsorted list and compares each element to its adjacent number to check if the left element is bigger than the right element. In case that is true, the elements swap their positions. The list is then iterated as many times as needed until the list is completely sorted. It is named "bubble" because of the way that the larger numbers "rise" like bubbles.

Despite being ease to code and to understand, this is the least efficient sorting algorithm of the program, since it needs to iterate through the list too many times, giving it a O(n^2) comparisons in the worst case scenario. This can be observed in this program as Bubble sort takes upwards to 2 minutes to sort a 10,000 elements list! That is why Bubble sort is not recomended for larger databases.

# To do list
There is still a lot of work to be done at the time of posting. I am still quite a beginner, so it might take a while.
I am still going to add:

- More sorting algorithms
- Comments and documentation
- Optimization of overall code
- Bug fixes
