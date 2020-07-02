import urllib.request
from flask import Flask, json

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_main():
    res = {
        "status": "success",
        "error": False,
        "api": [
            "/activities",
            "/positions",
            "/form"
        ]
    }

    return json.dumps(res)

@api.route('/activities', methods=['GET'])
def get_activities():
    with urllib.request.urlopen("https://pastebin.com/raw/bs6RK1Wv") as url:
        data = json.loads(url.read().decode())
        return json.dumps(data)

@api.route('/positions', methods=['GET'])
def get_positions():
    with urllib.request.urlopen("https://pastebin.com/raw/mCadhQ0Y") as url:
        data = json.loads(url.read().decode())
        return json.dumps(data)

@api.route('/form', methods=['GET'])
def get_form():
    with urllib.request.urlopen("https://pastebin.com/raw/xGFK8TvB") as url:
        data = json.loads(url.read().decode())
        return json.dumps(data)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=443)