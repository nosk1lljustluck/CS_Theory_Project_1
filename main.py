#Euclidean Algorithm to calculate GCD(greatest common divisor)


#declare first number
number_1=24

#declare the second number
number_2=12


#create a function to calculate GCD of two numbers using euclidean algorithm to make sure our code is reusable
def euclidean_algorithm(first_number, second_number):
    
    #create one other variable to keep track of remainder
    remainder=0
    
    #create while loop
    while (first_number!=0 and second_number!=0): 
        #loop infinitely until one of the two given numbers become zero
        
        #find the remainder when first_number is divided by second_number
        remainder=first_number%second_number
        
        #set second_number to first_number
        first_number=second_number
        
        #set remainder to second_number
        second_number=remainder
        
    #return both numbers
    return first_number, second_number
    
#call the function using two parameters and set the returning values to new variables
new_number_1, new_number_2 = euclidean_algorithm(number_1, number_2)

#check which number is zero and print out the non-zero one
if new_number_1==0:
    print(new_number_2)
else:
    print(new_number_1)
    



