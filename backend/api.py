# file backend/api.py
from flask import Flask
from flask import jsonify
from flask import request, send_from_directory

app = Flask(__name__, static_url_path='')

# this function returns an object for one user
def u(user_id):
    return {
        "type": "users",                    # It has to have type
        "id": user_id,                      # And some unique identifier
        "attributes": {                     # Here goes actual payload.
            "info": "data" + str(user_id),  # the only data we have for each user is "info" field
        },
    }

# routes for individual entities
@app.route('/api/users/<user_id>')
def users_by_id(user_id):
    return jsonify({"data": u(user_id)})

# default route.
# flask has to serve a file that will be generated later with ember
# relative path is backend/static/index.html
@app.route('/')
def root():
    return send_from_directory('static', "index.html")


# route for all entities
@app.route('/api/users')
def users():
    return jsonify({
        "data": [u(i) for i in range(0,10)]
        })

# route for other static files
@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)


if __name__ == '__main__':
    print("use\n"
          "FLASK_APP=dummy.py python -m flask run\n"
          "instead")
    exit(1)
