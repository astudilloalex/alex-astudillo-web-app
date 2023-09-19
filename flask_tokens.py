pip install Flask
pip install PyJWT

from flask import Flask, request, jsonify
import jwt


app = Flask(__name__)

# Replace 'your_private_key' and 'your_public_key' with your actual RSA key pair, please do not save on code, use separated files to manage keys
PRIVATE_KEY = 'your_private_key'
PUBLIC_KEY = 'your_public_key'

# Replace 'your_issuer' with your desired issuer value
ISSUER = 'your_issuer'

@app.route('/get_token')
def get_token():
    # Create a payload with user data
    user_data = {
        'user_id': 123,
        'username': 'example_user'
    }

    # Create a JWT token with the payload, private key, and issuer using RS256
    token = jwt.encode({'data': user_data, 'iss': ISSUER}, PRIVATE_KEY, algorithm='RS256')

    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

# Replace 'your_public_key' with your actual RSA public key, do not save on this part use other file to save this.
PUBLIC_KEY = 'your_public_key'

@app.route('/protected', methods=['GET'])
def protected_route():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"message": "Token is missing"}), 401

    try:
        # Verify and decode the JWT token using the public key and RS256 algorithm
        decoded_token = jwt.decode(token, PUBLIC_KEY, algorithms=['RS256'])
        user_id = decoded_token['data']['user_id']
        return jsonify({"message": f"This is a protected route for user {user_id}"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.DecodeError:
        return jsonify({"message": "Token is invalid"}), 401

if __name__ == '__main__':
    app.run(debug=True)


# Separate files for flask
my_flask_app/
│   app.py
│
├── controllers/
│   ├── __init__.py
│   ├── user_controller.py
│   └── country_controller.py

# controllers/user_controller.py
from flask import Blueprint, jsonify

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users', methods=['GET'])
def get_users():
    # Logic to get users
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Alice'}]
    return jsonify(users)

# Add more routes and controllers related to users here

# controllers/country_controller.py
from flask import Blueprint, jsonify

country_controller = Blueprint('country_controller', __name__)

@country_controller.route('/countries', methods=['GET'])
def get_countries():
    # Logic to get countries
    countries = [{'id': 1, 'name': 'USA'}, {'id': 2, 'name': 'Canada'}]
    return jsonify(countries)

# Add more routes and controllers related to countries here


# app.py
from flask import Flask
from controllers.user_controller import user_controller
from controllers.country_controller import country_controller

app = Flask(__name__)

# Register the controllers in the application
app.register_blueprint(user_controller, url_prefix='/users')
app.register_blueprint(country_controller, url_prefix='/countries')

if __name__ == '__main__':
    app.run(debug=True)


{
  "private_key": "-----BEGIN PRIVATE KEY-----\nYourPrivateKeyHere\n-----END PRIVATE KEY-----\n",
  "public_key": "-----BEGIN PUBLIC KEY-----\nYourPublicKeyHere\n-----END PUBLIC KEY-----\n"
}

with open('private_key.json', 'r') as private_key_file:
    private_key = json.load(private_key_file)["private_key"]


from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS
cors = CORS(app, resources={r"/api/*": {"origins": "http://example.com"},
                            r"/other/*": {"origins": "https://example2.com"},
                            r"/all/*": {"origins": "*"},
                            },
            allow_headers=["Content-Type", "Authorization"],
            supports_credentials=True,
            )

# Example route
@app.route('/api/data')
def get_data():
    return jsonify({"message": "This data is CORS-enabled for http://example.com"})

if __name__ == '__main__':
    app.run()
