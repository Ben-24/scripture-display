import random

class Scriptures():
    def __init__(self):
        # List of scriptures
        self.scriptures = ["1 Cor 1:1-3", "John 3:16"]
        
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