from flask import Flask, request as req, jsonify
import mybackend as backend

app = Flask(__name__)

@app.route('/', methods=['GET'])
def webservice():
    startlocation = req.args.get('startlocation')
    timeduration = req.args.get('timeduration')
    k = req.args.get('k')
    print(startlocation," ", timeduration)
    res = ['ron','yuval']
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
