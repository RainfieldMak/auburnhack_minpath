

class Event:
    
    def __init__(self, place, time):

        #place: string , name of place
        #time : tuple, e.g. [star_time , end_time], where start_time and end_time is in string , 24 hour format e.g. 2300

        self.place=place
        self.start_time=time[0]
        self.end_time=time[1]
        


    def get_place(self):
        return self.place
    
    def get_start (self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def to_string(self):
        return self.get_place() +" "+ self.get_start()+" " + self.get_end_time()
    



    
if __name__ == "__main__":

    test1=Event("uab", ["0000", "0100"])
    print(test1.to_string())