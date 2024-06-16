# Scripture Display
This is code for a project I made using a Raspberry Pi Pico W to run a 0.91 inch OLED display that shows a scripture of the day out of 42 scriptures and a daily goal that is fetched from my Notion database.

# Getting it Working
The Pico W needs to have micropython-ssd1306 installed as the driver. Any screen using that driver will work, you just have to set it to the proper resolution inside of screen.py.
Scriptures can be editted inside of Scripture.py.
Sensitive WIFI and Notion parameters are set in a file you create called user_info.json. It needs to be configured as follows:
```
{
    "wifi_parameters": {
        "ssid": "WIFI_NAME", 
        "password": "WIFI_PASSWORD"
    },
    "notion_parameters": {
        "auth": "NOTION_AUTHENTICATION_TOKEN",
        "database_id": "NOTION_DATABASE_ID"
    }
}
```
