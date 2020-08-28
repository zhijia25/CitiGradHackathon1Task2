from flask import Flask


app = Flask(__name__, static_url_path="")


@app.route('/')
def hello_world():
    print("received request")
    return 'Hello, World!'


if __name__ == '__main__':
    app.run("localhost", "8080", debug=True)
