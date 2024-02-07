#Kevin Gabari 
#7 Feb 2023
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder

#define the funciton header called divisors expecting one argument
def divisors(num):
    
    myList = []
    
    for i in range(1, num):
        if num % i == 0:
         
            myList.append(i)
    return myList
print(divisors(20))



            
            
 
   
    
