from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/say/flask')
def dojo():
    return "Hi Flask!"

@app.route('/say/michael')
def a():
    return "Hi Michael!"

@app.route('/say/john')
def b():
    return "Hi John!"

@app.route('/repeat/35/hello')
def c():
    return "hello \n" * 35

@app.route('/repeat/80/bye')
def d():
    return "bye \n" * 80

@app.route('/repeat/99/dogs')
def e():
    return "dogs \n" * 99

@app.route('/dojo')
def f():
    return "Dojo!"



if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.
