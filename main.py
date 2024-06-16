from screen import Screen
from notion import Notion
from scriptures import Scriptures
import time
from machine import lightsleep # type: ignore
import json

def main():    
    # Get user information from the user_info.json
    user_info_file = 'user_info.json'
    
    with open(user_info_file, 'r') as f:
        user_info = json.load(f)
    
    # Initialize notion object and set initial goal
    notion = Notion(user_info["wifi_parameters"], user_info["notion_parameters"])
    notion.connect_to_wifi()
    goal = notion.get_daily_goal()
    notion.disconnect_from_wifi()   
    
    # Initialize scriptures object and get the first scripture
    scrips = Scriptures()
    daily_scrip = scrips.get_random_scripture() 
    
    # Initialize screen and write goal and scripture to screen
    oled = Screen()
    oled.write_wrapped_text(daily_scrip)
    oled.write_wrapped_text(goal)
    
    # Lightsleep time variables
    ten_ms = 10
    ten_seconds_in_ms = 10000
    one_minute_in_ms = 60000
    twelve_hours_in_ms = 43200000
    first_half = True
    
    # while (1):       
        # Sleep to give screen time to process
        time.sleep(1)
        print("sleep")
        lightsleep(twelve_hours_in_ms)
        
        # Get daily goal
        notion.connect_to_wifi()
        goal = notion.get_daily_goal()
        notion.disconnect_from_wifi()
        
        # Get daily scripture
        if (first_half):
            daily_scrip = scrips.get_random_scripture() 
            first_half = False
        
        # Change display
        oled.clear_screen()
        oled.write_wrapped_text(daily_scrip)
        oled.write_wrapped_text(goal)
        
if __name__ == "__main__":
    main()
