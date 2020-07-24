#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Run time complexity of this is linear - O(n).

The variable a that being set the first time and the second time will always be O(1), but the while loop will be linear time base on the input of n.

The greater the input n is, the longer it will take to run the function. And because we don't care about constant when calculating big O, therefore this result in the run time of O(n)

a = 0                       # O(1)
while (a < n * n * n):      # O(n)
    a = a + n * n           # O(1)

b) Run time complexity of this is quadratic - O(n^2)

Every variables that being store/modified in this function will always have the big O(1), and the for loop and the while loop will be linear time based on the input n.

However, since there is a while loop inside of a for loop, this will actually make this a big O(n^2). Because for every single element i in the for loop, there will be not just one, but many element j for that specific i element. Therefore this will have the run time of O(n^2)

sum = 0             # O(1)
for i in range(n):  # O(n)
    j = 1           # O(1)
    while j < n:    # O(n)
        j *= 2      # O(1)
        sum += 1    # O(1)

The run time of this will be O(n^2)

c) Run time complexity of this is linear - O(n)

This is a recursive algorithm, a function that calls itself. 

Base on the size of the input, we can predict that it run time will always depends on it. 

Our base case here is when bunnies == 0, so if our input was 1 then the second return of this function will change the input to 0, and now we hit the base case.

But if our input was larger, then it would take more time for the function itself to hit its base case.

def bunnyEars(bunnies): 
    if bunnies == 0:                    # O(1)
        return 0

    return 2 + bunnyEars(bunnies-1)     # O(n)

## Exercise II

Since we don't know how high the n building would be, and f could be any where near the top or the bottom of the building, I think using a binary search would be best solve this problem. 

By using the binary search, we can eliminate the amount of time to figure out the value of f by halving our input everytime.

First off we need to figure out what the mid point of the building is, then we can start dropping egg.

If egg is broken when dropped in the mid point, we now can look at the lower levels of the building, using the same method, find a new mid point of the lower levels.

However, if egg didn't break at our first mid point, then we can ignore the bottom levels and start looking at the top levels istead.

Repeat the method until we find out what f is.

The run time complexity of this solution will be O(log n)

def find_f(n, f):
    start = 0
    end = len(n) - 1

    while end > start:
        mid = (end + start) // 2

        if n[mid] == f:
            return mid

        else:
            if f < n[mid]:
                end = n[mid] - 1
            else:
                start = n[mid] +1

    return -1