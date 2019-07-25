#BIG Sorted array from 2 small sorted arrays

def big_sorted_array(first_small_sorted_array, second_small_sorted_array):
    big_sorted_array = []
    while(len(first_small_sorted_array) > 0 or len(second_small_sorted_array) > 0):
        if(len(second_small_sorted_array) == 0):
            big_sorted_array += first_small_sorted_array
            first_small_sorted_array = []
        elif(len(first_small_sorted_array) == 0):
            big_sorted_array += second_small_sorted_array
            second_small_sorted_array = []
        else:
            if(first_small_sorted_array[0] < second_small_sorted_array[0]):
                big_sorted_array.append(first_small_sorted_array[0])
                del first_small_sorted_array[0]
            else:
                big_sorted_array.append(second_small_sorted_array[0])
                del second_small_sorted_array[0]
                
    return big_sorted_array

arr1 = [-10, -4, -1, 0, 22, 44]
arr2 = [-100, -99, -2, 1, 21, 96, 101]
print(big_sorted_array(arr1, arr2))    
                
                
                
                