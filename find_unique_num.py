def find_uniq(arr):
    # your code here
    n = 0
    counter = 0
    
    # using nasted loop
    # 1st loop used to loop the entire value
    for index in range(len(arr)):
        target = arr[index]
        
        # 2nd loop used to find the unique
        for num in arr:
            if (num == target):
                counter+=1 
                
            # if the number found twice, then skip to next number
            if (counter >= 2):
                counter = 0
                break
        
        # at the end of 2nd loop
        # if the counter is equal to 1
        # then it is 
        if (counter == 1):
            n = target
            break
        
    return n   # n: unique number in the array