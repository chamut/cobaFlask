from flask import Flask, request
from flask_cors import CORS
from cobalagi import Cobalagi

app = Flask(__name__)
CORS(app)

respon = {"result": ""}


def handle_respon(id, nama):
    namaa = id, nama
    respon["result"] = namaa
    return respon

@app.route("/a")
def helloWorld():
    return "Hello, cross-origin-world!"


@app.route("/", methods=['GET'])
def helloWorldpost():
    #id = request.get_json()
    respon3 = Cobalagi().getdata()
    #respon2 = handle_respon(id["id"], id["nama"])
    respon3 = {"data" : respon3}
    return respon3


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1278)
