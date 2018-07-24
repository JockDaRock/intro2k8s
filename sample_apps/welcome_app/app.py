from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def main():
    name = os.getenv("your_name", default="You wonderful person, you")
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
