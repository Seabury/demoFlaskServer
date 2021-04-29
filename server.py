from flask import Flask, render_template
app = Flask(__name__)

import csv

baseURL = "http://firebase.com"


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/students')
def get_students():

    with open('./static/data.csv') as f:
        students = [{k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]

    return render_template("students.html", students=students)

@app.route('/student/<studentName>')
def get_student(studentName):

    with open('./static/data.csv') as f:
        students = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]

    result = {}

    for student in students:
        if student["name"] == studentName:
            result = student

    if result:
        return render_template("student.html", student=result, baseURL=baseURL)
    else:
        return "404"