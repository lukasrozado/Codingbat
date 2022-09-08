#Given an array of ints, return True if the sequence of numbers 1, 2, 3 
# appears in the array somewhere.

#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True


def array123(nums):
    array_nums = len(nums)
    #START - 2 SO TO CHECK IN THE ARRAYS IF DOENST EXIST AND BE ABLE TO ITERATE IN THE LOOP
    for numbers in range(array_nums-2):
        if nums[numbers] == 1 and nums[numbers+1] == 2 and nums[numbers+2] == 3:
            return True
    return False