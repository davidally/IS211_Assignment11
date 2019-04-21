from flask import Flask
app = Flask(__name__)

task_list = []


@app.route('/')
def home():
    return 'hello world!'


if __name__ == '__main__':
    app.run()