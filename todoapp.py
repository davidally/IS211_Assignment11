from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

task_list = []
error_message = None


@app.route('/')
def home():
    return render_template('index.html',
                           task_list=task_list,
                           error_message=error_message)


@app.route('/submit', methods=['POST'])
def submission():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    validate = r'[^@]+@[^@]+\.[^@]+'
    if re.match(validate, email):
        task_list.append(task)
        return redirect('/')
    else:
        print 'ERROR'
        error_message = 'Please enter a valid email.'
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear_list():
    if task_list:
        del task_list[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()