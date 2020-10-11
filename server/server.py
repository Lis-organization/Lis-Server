from flask import Flask
from flask_cors import CORS, cross_origin
import sys
sys.path.append('..')
from main import replace_words_in_string, check_comands


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/lis/text=<text>", methods=['GET'])
@cross_origin()
def index(text):
	output_text = check_comands(replace_words_in_string(text))
	return output_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)