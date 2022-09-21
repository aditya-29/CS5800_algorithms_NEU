"""
    Solution for the Modular Exponentiation PS1 - CS5800 Algorithms
"""

# step 1 : get the inputs and convert them into integers
a,x,n = str(input()).split(" ")
a = int(a)
x = int(x)
n = int(n)



def get_binary_string(integer_number):
    """
        Method function to convert integers to binary string

    PARAMS:
        integer_number - (int) input integer

    RETURNS:
        binary_string - (str) binary string
    """

    if integer_number==0:                                               # check if a==0
        return integer_number

    binary_string = ""                                                  # initialize a empty string
    recursive_variable = integer_number

    while recursive_variable>0:                                         # loop till 'a' becomes zero
        binary_string = str(recursive_variable&1) + binary_string       # append last character to the string
        recursive_variable = recursive_variable>>1                      # left shit 'a'

    return binary_string                                                # return the binary string

def modular_exponentiation(a,x,n) :
    """
        Method to calculate the power of an integer

    PARAMS: 
        a - base integer
        x - power quotient  
        n - to be taken mod of
        
    RETURNS:
        calculated_out - return the output (a^x) mod n

    LOGIC:
        a = 2
        x = 10
        
        binary of x = 1010

        iter 1:
            bin_x = 101
            a = a*a = 4
        
        iter 2:
            out = out*a = 4
            bin_x = 10
            a = a*a = 16

        iter 3:
            bin_x = 1
            a = a*a = 256

        iter 4:
            out = out * a = 4*256 = 1024
            bin_x = 0
            a = a*a = 256^2

            return out
    """
    
    calculated_out = 1                                          # initialize the output variable to 1
    a = a % n                                                   # do a mod operation on the input once

    if (a == 0):                                                # if input = 0; return 0
        return 0
 
    while (x > 0) :                                             # loop until x > 0
        if (x & 1) == 1:                                        # check whether the number is odd
            calculated_out = (calculated_out * a) % n           # multiply the output by the number by a and take mod
 
        x = x >> 1                                              # left shit 'x' by 1
        a = (a * a) % n                                         # square the base number and take mod
            
    return calculated_out                                       # return the output


#### DRIVER CODE ####
print(get_binary_string(x))                                     # print the binary representation of 'x'
counter_variable = 1                                            # initialize variable 'counter_variable' = 1

while True:                                                     # create an inifinite loop
    if (counter_variable<=x):                                  
        print(modular_exponentiation(a,counter_variable,n))     # calculate the power mod n of the given numbers
        if counter_variable==x:
            break                                               # break the loop if 'counter_variable' equals 'x'
        counter_variable = counter_variable<<1                  # square the variable 'counter_variable'
    else:
        print(modular_exponentiation(a,x,n))                    # print the a^x mod n; if i becomes greater than x and break the loop
        break                                   
    