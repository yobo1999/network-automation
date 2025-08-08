from api_practice import api_request
import csv


def main():
    with open("network-automation/enterprise_list.csv", "r") as device:
        csv_reader = csv.DictReader(device)
        api = api_request()
        
        for line in csv_reader:
            api.add_device(line)
    
if __name__ == "__main__":
    main()
