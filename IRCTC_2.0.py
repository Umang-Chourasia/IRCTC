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

        print(boxed_text(" WELCOME TO INDIAN RAILWAYS "))
        self.API_key = api
        self.get_schedule()

    def get_schedule(self):
        train_number = input("\nEnter the train number to get its schedule: ")
        if len(train_number) != 5:
            print("Please enter only Indian train number with 5 digit.")
            exit(0)   
        print("\n")
        try:
            content = requests.get(f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/{self.API_key}/TrainNumber/{train_number}/")
            content.raise_for_status()
            train_schedule = json.loads(content.text)

            if train_schedule["ResponseCode"] == "200" and train_schedule["Status"] == "SUCCESS" and "Route" in train_schedule:
                with open("IRCTC.txt", 'w') as f:
                    f.write(json.dumps(train_schedule, indent=4))
                print(f"{'S.No.'.ljust(5)} {'Station Name'.ljust(25)} {'Arrival'.ljust(15)} {'Departure'}")
                print("-" * 65)
                counter = 1
                for station in train_schedule["Route"]:
                    print(f"{str(counter).ljust(5)} {station['StationName'].ljust(25)} {station['ArrivalTime'].ljust(15)} {station['DepartureTime']}")
                    counter += 1
            else:
                print(f"Error: Could not retrieve schedule for train number {train_number}. Response: {train_schedule.get('Message', 'Unknown error')}")

        except requests.exceptions.RequestException as e:
            print(f"Network error occurred: {e}")
        except json.JSONDecodeError:
            print("Error: Could not decode the API response.")
        except KeyError as e:
            print(f"Error: Missing key in the API response: {e}")

my = IRCTC("9039ce88e1e14e7ac5b863431355f921")