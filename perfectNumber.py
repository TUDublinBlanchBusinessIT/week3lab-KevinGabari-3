#Add your name here
#Add the date here
#Add the filename here

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

from divisors import divisors


def perfectNumber (x):
    result = False

    sum_of_divisors = sum (divisors(x))
                        
    if sum_of_divisors ==x:
            result = True 


    return result
