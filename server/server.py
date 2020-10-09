from flask import Flask
import sys
sys.path.append('..')
from main import replace_words_in_string, check_comands


app = Flask(__name__)

@app.route("/lis/text=<text>", methods=['GET'])
def index(text):
	output_text = check_comands(replace_words_in_string(text))
	return output_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)