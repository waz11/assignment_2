import flask
from flask import Flask, request as req, jsonify
import mybackend as backend
from mybackend import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET'])
def webservice():
    startlocation = req.args.get('startlocation')
    timeduration = req.args.get('timeduration')
    k = req.args.get('k')
    print(startlocation," ", timeduration)
    res = get_recommendations(startlocation, timeduration, k)
    # return flask.Response(jsonify(res), status=200)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
