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
    print task_list
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear_list():
    task_list = []
    print task_list
    return render_template('index.html', task_list=task_list)


if __name__ == '__main__':
    app.run()