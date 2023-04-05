from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the root endpoint of your API
@app.route('/')
def index():
    return 'Hello from flask API'

# Define a route for a simple GET endpoint
@app.route('/api/get', methods=['GET'])
def get_data():
    data = {'message': 'This is a sample response.'}
    return jsonify(data)

# Define a route for a POST endpoint that accepts JSON data
@app.route('/api/post', methods=['POST'])
def post_data():
    req_data = request.get_json()
    message = req_data['message']
    response_data = {'message': f'Received message: {message}'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
