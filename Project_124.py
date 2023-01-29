from flask import Flask,jsonify, request

app = Flask(__name__)
print(__name__)

#Normal strings in Python are stored internally as 8-bit ASCII, 
# while Unicode strings are stored as 16-bit Unicode. 
# This allows for a more varied set of characters, 
# including special characters from most languages in the world.
tasks = [
    {
        'id': 1,
        'Name': u'Chinmay',
        'Contact': u'9293191082', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Ajay',
        'Contact': u'8310129372', 
        'done': False
    },
    #add task
]


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/AddData", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

#tasks[-1]: returns the last task. In python, positions can be referred with 
#index 0,1,2.. or -1,-2,-3..(reverse)

#Adding a new task
    task = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json['Contact'],
        'done':False
    }
    tasks.append(task)
    return jsonify({
            "status":"Success",
            "message": "Task Added Successfully !"
        })


#Code for GET Api
@app.route("/GetData")
def gettask():
    return jsonify({
        "data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)