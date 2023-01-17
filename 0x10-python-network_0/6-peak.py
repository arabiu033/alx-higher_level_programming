#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):

  if (not len(list_of_integers)):
    return None
  # Use anoher function so as to call it appropriately
  return peak(list_of_integers, 0, len(list_of_integers) - 1)

# Ueing recursive binary search
def peak(arr, start, end):
  # we've reache to the begining of the array
  if (start >= end):
    return arr[end]
  
  # Obtain the middle index
  mid = int(start + (end - start) / 2)

  # check
  if (arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
    return arr[mid]
  elif (arr[mid] < arr[mid+1]):
    return peak(arr, mid+1, end)
  else:
    return peak(arr, start, mid-1)

# print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))