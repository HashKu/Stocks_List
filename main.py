from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

tasks = [
   {}
]

@app.route('/')
def home():
    # templates/home.html
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    value = request.form['value']
    task = {'name': name, 'finished': value}
    tasks.append(task)
    return render_template('home.html', tasks=tasks) 

@app.route('/delete/<int:id>')
def delete(id):
    del tasks[id]
    return render_template('home.html', tasks=tasks)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    value = request.form['value']
    #id = int(request.form['id'])
    task = {'name': name, 'finished': value}
    tasks[id] = task
    print(request.form)
    return redirect(url_for('home'))


app.run(debug=True)

