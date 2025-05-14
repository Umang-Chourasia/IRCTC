import requests
import json

def boxed_text(text):
    length = len(text)
    line1 = " " * 30 + '+' + '-' * (length + 2) + '+'
    line2 = "*" * 30 + f'| {text} |' + "*" * 30
    line3 = " " * 30 + '+' + '-' * (length + 2) + '+'
    return f"{line1}\n{line2}\n{line3}"

class IRCTC:
    def __init__(self, api):
         
        print(boxed_text(" WELCOME TO INDIAN RAILWAYS "), end = "")
        self.API_key = api
        self.get_schedule()

    def get_schedule(self):
        
        train_number = input("\n\nEnter the train number: ")
        print("\n")
        content  = requests.get(f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/{self.API_key}/TrainNumber/{train_number}/")
        
        train_schedule = json.loads(content.text)
        
        with open("IRCTC.txt", 'w') as f:
            f.write(json.dumps(train_schedule, indent=4))
            counter = 1
            for station in train_schedule["Route"]:
                print(f"{counter} \t\t {station['StationName']} \t\t {station["ArrivalTime"]} \t\t {station["DepartureTime"]}")
                counter +=1

api = input("Enter you API key: ")
my = IRCTC(api)