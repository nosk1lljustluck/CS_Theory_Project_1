#Euclidean Algorithm to calculate GCD(greatest common divisor)

#declare two variables to store values from user
number_1=int()
number_2=int()

#create one flag variable to check if inputs are valid
flag=False

#create while loop to ask for user input until they enter valid numbers
while (not flag):
    
    #take inputs from the user
    number_1=int(input("Enter the first number (non-negative): "))
    number_2=int(input("Enter the second number (non-negative): "))
    
    
    #store the result to flag, whether they are valid or not
    #standard euclidean algorithm cannot find the GCD of negative number and two zeros
    flag = (number_1>=0 and number_2>=0) and (number_1!=0 and number_2!=0)
    
    #print out the error message if inputs are invalid
    if (not flag):
        print("You entered invalid inputs, do not use negative numbers or two zeros!")


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
    print(f"GCD of {number_1} and {number_2}: {new_number_2}")
else:
    print(f"GCD of {number_1} and {number_2}: {new_number_1}")
    



