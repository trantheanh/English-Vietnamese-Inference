from __future__ import print_function
from future.standard_library import install_aliases
from flask import Flask, request, make_response
from flask_cors import CORS
import json
import os
from bot import translation

install_aliases()
app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return "Welcome to Wisdom Seeker! 19:26"

@app.route('/api/translate', endpoint='translate', methods=['POST'])
def translate():
    raw_request = request.get_json(silent=True, force=True)
    input = raw_request["input"]
    output = translation(input)
    response = generate_response(0, output)
    return response

def generate_response(code=0, output=None):
    response = {'code': code, 'message': '', 'output': output}
    res = json.dumps(response)
    response = make_response(res)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print("Starting app on port %d" % port)
    app.run(threaded=True, debug=False, port=port,host = '0.0.0.0')