#Get sequence of numbers with maximum sum of its members from array

def max_seq(arr):
    max = arr[0]
    sum = 0
    sequence_first_element = 0
    sequence_last_element = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i,j+1):
                sum += arr[k]
            if sum > max:
                max = sum
                sequence_first_element = i
                sequence_last_element = j
            sum = 0

    return(sequence_first_element, sequence_last_element)
    
def AssertEqual(expected_result, generated_result):
    if expected_result != generated_result:
        raise AssertionError("Expected:d {}, got: {}".format(expected_result, generated_result))
    else:
        print("Test case passed")
        

AssertEqual((0, 0), max_seq([1]))
AssertEqual((0, 2), max_seq([1, 2, 3]))
AssertEqual((1, 6), max_seq([-1, 0, 0, 0, 0, 0, 1]))
AssertEqual((5, 5), max_seq([-5, -10, -20, -4, -2, -1]))
AssertEqual((3, 4), max_seq([-4, -1, -5, 1, 2, -2, 2]))
print("All tests passed")        
        


    

    
    