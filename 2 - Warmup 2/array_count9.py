#Given an array of ints, return the number of 9's in the array.


#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    #SETUP TO LOCK IN 4 INSIDE THE ARRAY
    array_nums = len(nums)
    count = 0
    #LOOP OVER ALL NUMBERS IN THE ARRAY IN EVERY RANGE UNTIL FIND THE 9
    for numbers in range(array_nums):
        if nums[numbers] == 9:
            count += 1
    return count
