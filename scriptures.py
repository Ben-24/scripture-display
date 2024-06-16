import random

class Scriptures():
    def __init__(self):
        # List of scriptures
        self.scriptures = ["1 Cor 1", "John 3:16", "Col 1:15-23", "Phil 2:5-11", "Gal 2:19-21", "1 Thess 2:3,8,19", 
                           "2 Tim 4:7-8", "2 Tim 3:5,16", "Heb 1", "Heb 2:9-11,17-18", "Heb 4:14-16", "Heb 8:1-7",
                           "James 1:5-8", "James 2:14-26", "1 Pet 1:3-9", "1 Pet 1:13-16", "1 Pet 3:8-17", "1 Pet 4:1-6",
                           "1 Pet 4:16-19", "2 Pet 1:3-10", "1 John 1:5-10", "1 John 2:3-6", "1 John 2:22-25", "1 John 3:1-3",
                           "1 John 3:16-24", "1 John 4:7-21", "Rev 1:5-8", "Rev 19:1-10", "Rev 21:1-8", "Acts 1:6-11",
                           "Acts 3:17-21", "Acts 5:34-42", "Acts 7:54-60", "Acts 10:34-43", "Acts 13:2-4", "Acts 14:8-11",
                           "1 Cor 2:6-11", "1 Cor 6:12-20", "1 Cor 8:9-13", "1 Cor 10:12-17", "1 Cor 12:12-26", "1 Cor:15:3-11",
                           "1 Cor 15:54-58"]
        
        # List of scriptures not yet used's indexes
        self.scriptures_available = [i for i in range(len(self.scriptures))]
    
    def get_random_scripture(self):
        # If no scriptures available, reset the available scriptures
        if len(self.scriptures_available) == 0:
            self.scriptures_available = [i for i in range(len(self.scriptures))]
        
        # Return a random scripture as a string
        print(len(self.scriptures_available) - 1)
        index = random.randint(0, len(self.scriptures_available) - 1)  
        return self.scriptures[self.scriptures_available[index]]     