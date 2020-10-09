from flask import Flask
app = Flask(__name__)

@app.route("/lis/text=<text>", methods=['GET'])
def index(text):
    return "Hello, %s!" % text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)