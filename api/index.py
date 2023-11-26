# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Daeeee Mundo!'

# @app.route('/about')
# def about():
#     return 'About'


# Import Flask library
from flask import Flask, request, jsonify

# Create a Flask app object
app = Flask(__name__)

# Define a method to handle GET requests at the root path
@app.route("/", methods=["GET"])
def hello():
    # Return a simple greeting message
    return "Hello, this is a Flask server!"

# Define a method to handle POST requests at the /add path
@app.route("/add", methods=["POST"])
def add():
    # Get the JSON data from the request body
    data = request.get_json()
    # Extract the two numbers to be added
    num1 = data["num1"]
    num2 = data["num2"]
    # Calculate the sum of the two numbers
    result = num1 + num2
    # Return the result as a JSON object
    return jsonify({"result": result})

# Define a method to handle PUT requests at the /reverse path
@app.route("/reverse", methods=["PUT"])
def reverse():
    # Get the JSON data from the request body
    data = request.get_json()
    # Extract the string to be reversed
    string = data["string"]
    # Reverse the string using slicing
    reversed_string = string[::-1]
    # Return the reversed string as a JSON object
    return jsonify({"reversed_string": reversed_string})

# Run the app on port 5000
if __name__ == "__main__":
    app.run(port=5000)
