from flask import Flask, request as req, jsonify
from database_func import Database
from mybackend import get_recommendations

app = Flask(__name__)


# get endpoint of webservice for getting recomendations
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
    db = Database()
    app.run(debug=True,port=5000)
