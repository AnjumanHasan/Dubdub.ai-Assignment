from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# PMAK-63f13f9b568b6f64e8e1ea01-4db947240b6309d960205d3a922abaf550
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
#creating databse

db=SQLAlchemy(app)
ma=Marshmallow(app)


class ToDo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Boolean, nullable=False, default=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) :
        return self.id


class ToDoSchema(ma.Schema):
    class Meta:
        fields=('id','task','desc','completed','date_created')

#creating instance of schema

todo_schema=ToDoSchema(many=False)  #For selecting single record
todos_schema=ToDoSchema(many=True)  #for selecting multiple records


#Adding New Task (CREATE)
@app.route("/todo",methods=["POST"])

def add_task():

    try:
        task= request.json['task']
        desc=request.json['desc']

        newTask=ToDo(task=task,desc=desc)

        db.session.add(newTask)
        db.session.commit()
        return todo_schema.jsonify(newTask)

    except Exception as e:
        return jsonify({"Error:","Invalid"})
        
#get all tasks
@app.route("/todo",methods=["GET"])
def getAllTasks():
    tasks=ToDo.query.all()
    result_set=todos_schema.dump(tasks)
    return todos_schema.jsonify(tasks)


#get particular tasks based on id (READ)
@app.route("/todo/<int:id>",methods=["GET"])
def getTask(id):
    task=ToDo.query.get_or_404(int(id))
    return todo_schema.jsonify(task)


#update tasks based on id (UPDATE)
@app.route("/todo/<int:id>",methods=["PUT"])
def updateTask(id):
    updatedTask=ToDo.query.get_or_404(int(id))

    task=request.json['task']
    desc=request.json['desc']

    updatedTask.task=task
    updatedTask.desc=desc

    db.session.commit()

    return todo_schema.jsonify(task)

#deleting a task (DELETE)
@app.route("/todo/<int:id>",methods=["DELETE"])

def deleteTask(id):
    task=ToDo.query.get_or_404(int(id))
    db.session.delete(task)
    db.session.commit()

    return jsonify({"Success" : "Task deleted"})

#for marking the task as done/notdone
@app.route("/todo/mark/<int:id>",methods=["PUT"])
def complete(id):
    task=ToDo.query.get_or_404(int(id))
    if(task.completed==True):
        task.completed = False
    else:
        task.completed = True
    db.session.commit()

    return jsonify({"Updated ":"Task Done!"})


if __name__=="__main__" :
    app.run(debug=True)