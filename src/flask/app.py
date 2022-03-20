from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hi Valee"


# Make sure to set the environment variable as set FLASK_APP=app.py
# to enable development environment set FLASK_ENV=development

# to install flask enviornment first install python-dotenv and then create a .flaskenv file in your project root folder

if __name__ == '__main__':
    app.run(debug=True)