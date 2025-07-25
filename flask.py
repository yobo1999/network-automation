from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Username/password for demo
users = {
    "admin": "password"
}

@auth.get_password
def get_pw(username):
    return users.get(username)

devices = [
    {"hostname": "router1", "ip": "192.168.1.1", "type": "router", "os_version": "16.12.4", "ntp_configured": True}
]

@app.route('/devices', methods=['GET', 'POST'])
@auth.login_required
def device_collection():
    if request.method == 'GET':
        return jsonify(devices)
    elif request.method == 'POST':
        data = request.json
        for item in data:
            if item == data['hostname'] or item == data['ip']:
                return jsonify({"error:" "duplicate device"}), 409
            else:
                devices.append(data)
                return jsonify({"message": "Device added!", "device": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

