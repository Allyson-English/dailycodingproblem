# Get product of all other elements 

# April 30, 2021

# Prompt: given a list such as [1,2,3,4,5], function should return [120, 60, 40, 30, 24]

def product_otherelems(lst):
    
    # hold solutions in new list
    newlst = []

    # iterate through index and value in original list
    for idx, num in enumerate(lst):

        # select all elements except current one
        temp = [x for x in lst if not lst.index(x)==idx]
        result = 1
        
        # multiply all elements in temp together
        for ea in temp:
            result *= ea
        
        # append to solution
        newlst.append(result)
        
    return newlst


# Prompt: given an unsorted list, what is the smallest window that needs to be sorted (indexes that contain range of all numbers that require sorting)
# Goal was to not use native Python sorting


def check_sorted(lst):
    """ return True if list is sorted; otherwise, return False """
    
    for n in range(len(lst)-1):
        if lst[n] < lst[n+1]:
            pass
        else:
            return False
    
    return True

def sort(lst):
    """ swap sort (function for individual swaps, must be used in conjuction with while loop and function above """
    
    for n in range(len(lst)-1):
        if lst[n] > lst[n+1]:
            holder = lst[n]
            lst[n] = lst[n+1]
            lst[n+1] = holder
            
    return lst


def window(lst):
    """ function to generate solution """
    
    # make a deep copy of list passed to function
    orig_l = copy.deepcopy(lst)
    
    # sort the original list using functions defined above
    while not check_sorted(lst):
        lst = sort(lst)
    
    # zip original (unsorted) list with sorted list
    combined = list(zip(orig_l, lst))
    
    # list to hold results 
    wdw = []
    
    # enumerate through zipped list checked if numbers in each tuple are the same
    for idx, num in enumerate(combined):
        
        # if numbers are not the same, add index to results lists (wdw)
        if not num[0] == num[-1]:
            wdw.append(idx)
            
    # return first and last index of unsorted elements 
    return (wdw[0], wdw[-1])

# in any given array, find the greatest sum produced by a substring of contiguous elements

def contiguous_window(lst):
    
    sum_overallhighest = 0
    sum_currentpos = 0
    
    for num in lst:
        # used for determining maximum sum when there are negative values
        # is the value of the number greater than the value of the number plus the current sum?
        sum_currentpos = max(num, sum_currentpos+num)
        sum_overallhighest = max(sum_overallhighest, sum_currentpos)
            
    return sum_overallhighest
