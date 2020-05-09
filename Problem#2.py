# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

array = [1, 2, 3, 4, 5]

# this does it in O(n^2) time


def productArray(array):
    newArray = [1]*len(array)  # creates array of 1s

    print(newArray)
    for i in range(len(array)):
        for j in range(len(array)):
            if(j != i):
                newArray[i] *= array[j]  # finds the product excluding index

    return newArray


print(productArray(array))
