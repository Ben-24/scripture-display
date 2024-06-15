from screen import Screen
from notion import Notion
import time
from machine import lightsleep # type: ignore
import json

def main():    
    # Get user information from the user_info.json
    user_info_file = 'user_info.json'
    
    with open(user_info_file, 'r') as f:
        user_info = json.load(f)
    
    # Initialize wifi, connect to notion, retrieve daily goal
    notion = Notion(user_info["wifi_parameters"], user_info["notion_parameters"])
    notion.get_time()
    goal_data = notion.get_daily_goal()
    goal = goal_data['results'][0]['properties']['Name']['title'][0]['plain_text']
    notion.disconnect_from_wifi()    
    
    # Initialize screen and write goal and scripture to screen
    oled = Screen()
    oled.write_text(goal,0,0)
    oled.__del__()
    
    time.sleep(10)
    print("deep")
    lightsleep(100)
    
if __name__ == "__main__":
    main()
