'''
    Solution for the Modular Exponentiation PS1 - CS5800 Algorithms

    Team Members:
        1) Aditya Shanmugham (NUID : 002738073)
        2) Gugan Kathiresan (NUID : )
        3) Maria Anson (NUID : )
'''

# step 1 : get the inputs and convert them into integers
a,x,n = str(input()).split(" ")
a = int(a)
x = int(x)
n = int(n)



def cal_bin(a):
    '''
        Method function to convert integers to binary string

    PARAMS:
        a - input integer

    RETURNS:
        s - binary string
    '''

    if a==0:    # check if a==0
        return a
    s = ""
    while a>0:
        s = str(a&1) + s
        a=a>>1
    return s

print(cal_bin(x))

i = 1

def power(a,x,n) :
    out = 1  
    a = a % n
     
    if (a == 0) :
        return 0
 
    while (x > 0) :
        if (x & 1) == 1:
            out = (out * a) % n
 
        x = x >> 1     
        a = (a * a) % n
         
    return out

while True:
    if (i<=x):
        print(power(a,i,n))
        if i==x:
            break
        i = i<<1
    else:
        print(power(a,x,n))
        break
    