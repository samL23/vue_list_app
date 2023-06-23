from flask import Flask, jsonify, request
from flask_cors import CORS



todoList = ["Biking", "study science"]

 

#-------------------------------

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/todo', methods=['GET', 'POST'])
def all_items():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        todoList.append(post_data.get('item'))
        response_object['message'] = 'item added to Todo list'
    else:
        response_object = todoList
    return jsonify(response_object)
if __name__ == '__main__':
    app.run()