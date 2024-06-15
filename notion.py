import network # type: ignore
import time
import urequests # type: ignore # handles making and servicing network requests
import json

class Notion():

    def __init__(self, wifi_parameters, notion_parameters):
        # Set parameters
        self.ssid = wifi_parameters["ssid"] 
        self.password = wifi_parameters["password"]
        self.database_id = notion_parameters["database_id"]
        self.auth = notion_parameters["auth"]
        self.wlan = network.WLAN(network.STA_IF)
        
        self.connect_to_wifi()
    
    def __del__(self):
        # Disconnect from the internet upon deleting the object
        self.disconnect_from_wifi()
    
    def connect_to_wifi(self):
        # Connect to the WIFI
        print("Connecting to WiFi", end="")
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        while not self.wlan.isconnected():
            print(".", end="")
            time.sleep(0.1)
        print(" Connected!")
        print(self.wlan.ifconfig())
        
    def disconnect_from_wifi(self):
        # Disconnect from the internet
        self.wlan.disconnect()
        time.sleep(1)
        if not self.wlan.isconnected():
            print("Disconnected from WiFi")
        else:
            print("Failed to disconnect from WiFi")

    def get_time(self):
        response = urequests.get("https://worldtimeapi.org/api/timezone/America/Denver")
        data = response.json()
        # print(data)
        timestamp = data["datetime"]
        print(timestamp)
        return timestamp

    def get_daily_goal(self):
        headers = { 'Authorization' : f'Bearer {self.auth}',
                    'Notion-Version' : '2022-06-28',
                    'Content-Type': 'application/json',
                    }
        data = {"filter": {
                    "property": "Date",
                    "rich_text": {
                        "contains": f"2024-06-11",
                    },
                }}
        response = urequests.post(f"https://api.notion.com/v1/databases/{self.database_id}/query", headers=headers, data=json.dumps(data))
        text = response.text
        response.close()
        return json.loads(text)
    #['results'][0]['properties']['Name']['title'][0]['plain_text']