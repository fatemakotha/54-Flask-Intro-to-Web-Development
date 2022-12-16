import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

def say_hello():
    print("Hello")
@delay_decorator
def say_bye():
    print("Bye")
@delay_decorator
def say_thankyou():
    print("thankyou")

say_hello()
say_bye()
say_thankyou()

#------------or----------

decorated_function = delay_decorator(say_hello)
decorated_function()
