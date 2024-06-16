from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers: str):
    numbers_as_sum = (int(it) for it in numbers.split('/'))
    return f"Максимальное переданное число <i>{max(numbers_as_sum)}</i>"


if __name__ == '__main__':
    app.run(debug=True)
