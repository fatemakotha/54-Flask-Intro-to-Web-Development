from flask import Flask
app = Flask(__name__)

@app.route('/') #just one / means the user wants to see the home page. This is called a PYTHON DECORATOR
def hello_world():
    return 'Hello, World!'

print(__name__) #PRINTS: __main__
#Now if we import random and try to print that:
import random
print(random.__name__)
#--------------------------------------------------------------------------------------------------------------------------------
#--------After running the code, if it exits with 0----------
#--------Enter the following commands in the terminal, line by line----------
# set FLASK_APP=newfile.py
# $env:FLASK_APP = "newfile.py"
# flask run
#-----After the link opens for the website, BE SURE TO press ctrl+c to quit it-------

#--------------------OR----------------------


if __name__ == "__main__":
    app.run()
#--------------------------------------------------------------------------------------------------
#__name__ means the name of the file which in this case is the __main__ **

#--------------------------------------------------------------------------------------------------------------------------------

