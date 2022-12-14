#More about functions:
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#First class objects, can be passed around as arguements e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)
result = calculate(multiply, 2, 3)
print(result)
#--------------------------------------------------------------------------------------------------
#Nested functions:
def outer_function():
    print("I am outer")
    def nested_function():
        print("I am inner")
    nested_function()
# nested_function() #NameError: name 'nested_function' is not defined. Did you mean: 'outer_function'?
outer_function()
#PRINTS:# I am outer
        # I am inner
# *** YOU CANNOT CALL THE OUTER FUNCTION WITHOUT CALLING THE NESTED FUNCTION
#--------------------------------------------------------------------------------------------------
#Functions can be returned from other functions:
def outerr_function():
    print("I am outer func")
    def nestedd_function():
        print("I am inner func")
    return nestedd_function

innerr_func = outerr_function()
innerr_func()
#PRINTS:
# I am outer func
# I am inner func
