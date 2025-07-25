import requests
import getpass

url = "http://192.168.80.154:5000/devices"
new_device = {"hostname": "Router2", "ip": "192.168.1.2", "ntp_configured": True, "os_version": "16.12.4", "type": "router"}
def authenticate():
    username = input('Enter your username: ')
    password = getpass.getpass("Enter your password: ")
    return username,password


def get_devices():
    print('Starting Request')
    username, password = authenticate()
    response = requests.get(url, auth= (username, password), timeout=5)
    try:
        if response.status_code == 200:
            print(f"\n\n{username} authenticated")
        print(f"\n\n{response.json()}")
    except Exception as e:
        print("user could not be authenticated", e)

def add_device():
    print("Starting POST")
    username, password = authenticate()
    request = requests.post(url, auth=(username, password), timeout=5, json=new_device)
    try:
        print(request.status_code)
        if  request.status_code == 201:     
            print(f"\n\n {username} has added device")
            print("POST RESPONSE", request.json())
        elif request.status_code == 409:
            print("duplicate devices cannot be added")
        elif request.status_code == 401:
            print("authentication failed")
        else:
            print(f"Post from {username} could not be completed with error code {request.status_code}")
        
        
    except Exception as error:
        print(f"Unknown error", error)
    

add_device()
# get_devices()
# get_devices()
# if __name__ == "__main__":
        # main()
