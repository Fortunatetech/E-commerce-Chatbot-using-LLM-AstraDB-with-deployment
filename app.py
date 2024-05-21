from flask import Flask, render_template, request
from dotenv import load_dotenv
from src.retrieval_generation import generation
from src.data_ingestion import data_ingestion

app = Flask(__name__)

load_dotenv()

vstore=data_ingestion("done")
chain=generation(vstore)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)