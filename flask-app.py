from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Demo credentials
users = {
    "admin": "password"
}

# Flask-HTTPAuth expects a function for fetching passwords
@auth.get_password
def get_pw(username):
    return users.get(username)

# In-memory device list (starts with one hardcoded device)
devices = [
    {
        "hostname": "router1",
        "ip": "192.168.1.1",
        "type": "router",
        "os_version": "16.12.4",
        "ntp_configured": True
    }
]

@app.route('/devices', methods=['GET', 'POST'])
@auth.login_required
def device_collection():
    if request.method == 'GET':
        # Return all devices in the list
        return jsonify(devices)
    elif request.method == 'POST':
        data = request.json
        # Check for duplicates in hostname or IP
        for existing_device in devices:
            if (existing_device['hostname'] == data['hostname'] or
                existing_device['ip'] == data['ip']):
                return jsonify({"error": "duplicate device"}), 409
        # Not a duplicate: add the device
        devices.append(data)
        return jsonify({"message": "Device added!", "device": data}), 201

if __name__ == '__main__':
    # Run Flask on all interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)
