from flask import Flask
import socket

app = Flask(__name__)  # Corrected 'flask' to 'Flask'

@app.route('/')
def welcome():
    return 'Welcome to the website'

@app.route('/name')
def name():
    return 'ITD DevOps'

@app.route('/ip')
def ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)  # Corrected function name
    return f'Server IP Address: {ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the app on all available IPs on port 5000