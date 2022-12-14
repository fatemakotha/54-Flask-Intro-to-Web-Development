from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#--------After running the code, if it exits with 0----------
#--------Enter the following commands in the terminal, line by line----------

# set FLASK_APP=newfile.py
# $env:FLASK_APP = "newfile.py"
# flask run

#-----After the link opens for the website, BE SURE TO press ctrl+c to quit it-------