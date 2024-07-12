import flask

app = flask.Flask(__name__)

@app.endpoint('test')
def method_name():
    return "Test endpoint was called!"

if __name__ == "__main__":
    app.run()