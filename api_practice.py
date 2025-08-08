import requests
import getpass

class api_request:
    """

    Returns:
        _type_: _description_
    """
    
    def __init__(self):   
        self.url = "http://192.168.80.154:5000/devices"
        self.username = input('Enter your username: ')
        self.password = getpass.getpass("Enter your password: ")
     


    def get_devices(self):
        print('Starting Request')
        response = requests.get(self.url, auth= (self.username, self.password), timeout=5)
        try:
            if response.status_code == 200:
                print(f"\n\n{self.username} authenticated")
            print(f"\n\n{response.json()}")
        except Exception as e:
            print("user could not be authenticated", e)

    def add_device(self, device):
        print("Starting POST")
        post_request = requests.post(self.url, auth=(self.username, self.password), timeout=5, json=device)
        try:
            print(post_request.status_code)
            if  post_request.status_code == 201:     
                print(f"\n\n {self.username} has added device")
                print("POST RESPONSE", post_request.json())
            elif post_request.status_code == 409:
                print("Duplicate Device")
            else:
                print(f"Post from {self.username} could not be completed with error code {post_request.status_code}")


        except Exception as e:
            print(f"Unknown error", e)
    

#add_device()
#get_devices()
#get_devices()
# if __name__ == "__main__":
        # main()
