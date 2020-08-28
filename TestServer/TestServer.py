from flask import Flask


app = Flask(__name__, static_url_path="")


@app.route('/hello_world')
def hello_world():
    print("received request")
    return 'Hello, World!'


if __name__ == '__main__':
    app.run("172.20.10.7", "8080", debug=True)
