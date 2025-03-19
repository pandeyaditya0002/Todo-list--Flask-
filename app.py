from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
# Initialize the Flask application
app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the database
db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Home route to display and add todos
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # Get the title and description from the form
        title = request.form['title']
        desc = request.form['desc']
        # Create a new Todo object and add it to the database
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    # Query all todos from the database
    allTodo = Todo.query.all() 
    # Render the index.html template with the list of todos
    return render_template('index.html', allTodo=allTodo)

# Route to show all todos (for debugging purposes)
@app.route('/show')
def products():
    # Query all todos from the database
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

# Route to update a specific todo
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        # Get the updated title and description from the form
        title = request.form['title']
        desc = request.form['desc']
        # Query the todo by sno and update its title and description
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    # Query the todo by sno
    todo = Todo.query.filter_by(sno=sno).first()
    # Render the update.html template with the todo
    return render_template('update.html', todo=todo)

# Route to delete a specific todo
@app.route('/delete/<int:sno>')
def delete(sno):
    # Query the todo by sno and delete it from the database
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=8000)