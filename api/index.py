# Import Flask library
from flask import Flask, request
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import json

# Size of the answer, in number of words
answer_size = {"small": "150", "medium": "300", "large": "600"}

question_template = PromptTemplate(
    input_variables=["question", "age", "size", "language"],  # list of variables
    template="""You are an experienced teacher and when you answer any question, you follow these rules:
- Do it in a very didactic way
- Don't use any complicated words or an elaborate language
- Provide relevant and accurate information
- Give examples and illustrations when possible
- Check for understanding and feedback
- Focus only on the subject of the question asked
- Use about {size} words in your answer, but not less than that
- Explain to a {age} year old child
- Use {language} language as the medium of communication

Now you have to talk about the following subject:

{question}

Take a deep breath, and give an answer in a step-by-step way.

Answer:
"""
)

# Create a Flask app object
app = Flask(__name__)

# Define a method to handle GET requests at the root path
@app.route("/ask", methods=["POST"])
def ask():
    data = json.loads(request.get_data())

    question = data["question"]
    age = data.get("age", 5)
    size = data.get("size", "medium")
    temp = data.get("temp", 0.9)
    language = data.get("language", "Brazilian Portuguese")

    # llm = OpenAI(temperature = temp, max_tokens=int(answer_size[size]*2))
    llm = OpenAI(temperature = temp)
    question = question_template.format(question=question, age=age, size=answer_size[size], language=language)

    return llm(question)

# # Define a method to handle POST requests at the /add path
# @app.route("/add", methods=["POST"])
# def add():
#     # Get the JSON data from the request body
#     data = request.get_json()
#     # Extract the two numbers to be added
#     num1 = data["num1"]
#     num2 = data["num2"]
#     # Calculate the sum of the two numbers
#     result = num1 + num2
#     # Return the result as a JSON object
#     return jsonify({"result": result})

# # Define a method to handle PUT requests at the /reverse path
# @app.route("/reverse", methods=["PUT"])
# def reverse():
#     # Get the JSON data from the request body
#     data = request.get_json()
#     # Extract the string to be reversed
#     string = data["string"]
#     # Reverse the string using slicing
#     reversed_string = string[::-1]
#     # Return the reversed string as a JSON object
#     return jsonify({"reversed_string": reversed_string})

# Run the app on port 3000
if __name__ == "__main__":
    app.run(port=3000)
