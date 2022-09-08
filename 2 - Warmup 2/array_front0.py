#Given an array of ints, return True if one of the first 4 elements in the 
# array is a 9. The array length may be less than 4.

#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
    #SETUP TO LOCK IN 4 INSIDE THE ARRAY
    array_nums = len(nums)
    if array_nums > 4:
        array_nums = 4
    #LOOP OVER ALL NUMBERS IN THE ARRAY IN EVERY RANGE UNTIL FIND THE 9
    for numbers in range(array_nums):
        if nums[numbers] == 9:
            return True
    return False
