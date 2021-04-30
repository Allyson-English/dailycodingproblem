# Get product of all other elements

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
