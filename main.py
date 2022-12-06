from flask import Flask, render_template, request, redirect, url_for
import csv, instructions

app = Flask(__name__)


@app.route('/')
def home():
    tasks = instructions.load()
    return render_template('home.html', tasks=tasks)

def refresh():
    with open('informations.csv', newline='') as file_in:
        reader = csv.DictReader(file_in)
        tasks = []
        for row in reader:
            tasks += [row]
        return tasks


@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    value = request.form['value']
    buy_date = request.form['buy date']
    instructions.create(name, value, buy_date)
    return redirect("/")
    return render_template('home.html', task=tasks) 

@app.route('/delete/<id>')
def delete(id):
    retorno = instructions.delete(id)
    tasks = instructions.load()
    return render_template('home.html', tasks=tasks)


@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    value = request.form['value']
    id = request.form['id']
    buy_date = request.form['buy_date']
    retorno = instructions.update(id, name, value, buy_date)

    print(request.form)

    tasks = instructions.load()
    return render_template('home.html', tasks=tasks)


app.run(debug=True)

