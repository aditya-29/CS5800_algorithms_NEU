"""
    Solution for the Peak Detection PS2 - CS5800 Algorithms
"""

# declare a global variable 'ans'
ans = 0 


def div_conq(arr):
    '''
        Method function to apply the divide and conquer approach on the array

    PARAMS:
        arr - input array
    
    RETURNS:
        None

    Time Complexity : O(nlogn)
    Space Complexity : O(n)
    '''
    global ans

    if len(arr) > 1:
        mid = len(arr)//2       # find the mid index of the array
        
        l = arr[:mid]           # divide the left part of the array
        r = arr[mid:]           # divide the right part of the array

        div_conq(l)             # recursivey call the function on the left part of the array
        div_conq(r)             # recursivey call the function on the right part of the array

        print(l,r)

        c = 0
        i=j=k=0                 # initialise the loop variables

        while i<len(l) and j<len(r):    # perform merge sort on the array
            if l[i] <= r[j]:            
                arr[k] = l[i]
                i+=1
            else:
                print("first search")
                arr[k] = r[j]
                j+=1
                c+=i                  # count how many number in the left sub-array are greater than the right array
                
            k+=1
        
        while i<len(l):
            arr[k] = l[i]
            i+=1
            k+=1

        while j<len(r):
            c += i                    # count the remaining leftover elements in the right sub-array
            arr[k] = r[j]
            j+=1
            k+=1
            print("last elem : ")

        ans+=c

        print(c)

    return                              # End the recursive call


### DRIVER CODE ###

# n = int(input())                        # get the input 'n' from the user

# arr = input()                           # get the input 'arr' from the user 

n = 0
arr = [30,25,45,13,15,90,10]

if n==0:
    print(0)

# arr = arr.strip().split(" ")
arr = list(map(lambda x : int(x), arr)) # convert the string to array of integers

div_conq(arr)                           # function call for 'divide and conquer algorithm'
print(ans)                              # print the final answer

            
