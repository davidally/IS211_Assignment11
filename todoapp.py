from flask import Flask, render_template, request, redirect
app = Flask(__name__)

task_list = []


@app.route('/')
def home():
    return render_template('index.html', task_list=task_list)


@app.route('/submit', methods=['POST'])
def submission():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    task_list.append(task)
    return redirect('/')


if __name__ == '__main__':
    app.run()