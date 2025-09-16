from flask import Flask, request, jsonify

app = Flask(__name__)

# BUG: division by zero not handled
@app.route("/divide")
def divide():
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 0))  # default is zero → bug
    return jsonify({"result": a / b})

# TODO: Add /hello endpoint returning {"msg": "Hello, World!"}
if __name__ == "__main__":
    app.run(port=5000)
