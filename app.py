from flask import Flask, render_template, request, redirect

app = Flask(__name__)

FILE_NAME = "students.txt"

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Display Students
@app.route('/students')
def students():
    student_list = []

    try:
        with open(FILE_NAME, 'r') as file:
            student_list = file.readlines()
    except:
        pass

    return render_template('students.html',
                           students=student_list)

# Add Student (POST)
@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']

    with open(FILE_NAME, 'a') as file:
        file.write(name + "\n")

    return redirect('/students')

# Delete Student
@app.route('/delete/<name>')
def delete_student(name):

    try:
        with open(FILE_NAME, 'r') as file:
            students = file.readlines()

        with open(FILE_NAME, 'w') as file:
            for student in students:
                if student.strip() != name:
                    file.write(student)

    except:
        pass

    return redirect('/students')

if __name__ == "__main__":
    app.run(debug=True)