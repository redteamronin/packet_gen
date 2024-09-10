from flask import Flask, request, jsonify
import requests
from ping3 import ping
import threading
import time

# Prerequisites: pip install flask requests ping3

app = Flask(__name__)

# Route to handle GET requests
@app.route('/get', methods=['GET'])
def handle_get():
    return jsonify({"message": "GET request successful!"})

# Route to handle POST requests
@app.route('/post', methods=['POST'])
def handle_post():
    data = request.json
    return jsonify({"message": "POST request successful!", "data_received": data})

# Function to run the Flask server
def run_server():
    app.run(host='127.0.0.1', port=8888)

# Client function to send a GET request
def send_get_request():
    try:
        response = requests.get('http://127.0.0.1:8888/get')
        print(f"GET Response: {response.json()}")
    except Exception as e:
        print(f"Failed to send GET request: {e}")

# Client function to send a POST request
def send_post_request():
    data = {"name": "Client", "message": "Hello, Server!"}
    try:
        response = requests.post('http://127.0.0.1:8888/post', json=data)
        print(f"POST Response: {response.json()}")
    except Exception as e:
        print(f"Failed to send POST request: {e}")

# Client function to send ICMP ping
def send_icmp_ping():
    try:
        result = ping('127.0.0.1')  # Pinging localhost
        if result:
            print(f"Ping successful! Response time: {result} seconds")
        else:
            print("Ping failed.")
    except Exception as e:
        print(f"Failed to send ICMP ping: {e}")

if __name__ == '__main__':
    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Wait for the server to start
    time.sleep(2)

    while True:
        # Sending GET request
        print("Sending GET request...")
        send_get_request()

        # Wait 60 seconds
        time.sleep(60)

        # Sending POST request
        print("Sending POST request...")
        send_post_request()

        # Wait 60 seconds
        time.sleep(60)

        # Sending ICMP Ping
        print("Sending ICMP Ping...")
        send_icmp_ping()

        # Wait 2 minutes (120 seconds)
        time.sleep(120)
