#!flask/bin/python

from flask import Flask, jsonify, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Every Pizza is a personal pizza, if you try and think hard enogh"


message = [
    {
        'id': 1,
        'title': 'Hello World to Sauce Labs',
        'description': 'Peanut Butter cups are the best',
        'status': 'On route'
    }, {
        'id': 2,
        'title': 'This is to test the id and get_message',
        'status': 'I forgot statuses'
    }
]


@app.route('/helloworld/api/prakhar', methods=['GET'])
def get_message():
    return jsonify({'This is the content: ': message})


#redirects to the messages array with id 1 only else abort with 404
@app.route('/helloworld/api/prakhar/<int:msg_id>', methods=['GET'])
def get_mesasge(msg_id):
    msg = [msg for msg in message if msg['id'] == msg_id]
    if len(msg) == 0:
        abort(404)
    return jsonify({'task': msg[0]})


if __name__ == '__main__':
    app.run(debug=True)


