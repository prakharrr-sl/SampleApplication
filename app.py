#!flask/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Every Pizza is a personal pizza, if you try and think hard enogh"


message = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

if __name__ == '__main__':
    app.run(debug=True)
