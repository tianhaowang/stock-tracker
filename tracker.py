from flask import Flask, render_template
from werkzeug.security import check_password_hash
import database.user as db_user
from flask_cors import CORS
from flask import request, jsonify

app = Flask(__name__)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*", "allow_headers": "*"}})
app.config['CORS_HEADERS'] = '*'

@app.route('/users/login', methods=['POST'])
def user_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = db_user.login(username, password)
    if user:
        # Login successful
        return jsonify({'message': 'Login successful', 'user': user[0]}), 200
    else:
        # Login failed
        return jsonify({'error': 'Invalid username or password'}), 401
    


if __name__ == '__main__':
    app.run(port=7070)
