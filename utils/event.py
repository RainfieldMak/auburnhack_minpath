

class Event:
    
    def __init__(self, place, time,waypoint):

        #place: string , name of place
        #time : tuple, e.g. [star_time , end_time], where start_time and end_time is in string , 24 hour format e.g. 2300
        #half_hour_span: string , total no of half hour between start_time and end_time.
        #waypoint_order : integer , the order of waypoint , 0th base
        self.place=place
        self.start_time=time[0]
        self.end_time=time[1]
        self.half_hour_span= self.calculate_half_hours(self.get_start(), self.get_end_time())
        self.waypoint_order=waypoint
   
        

    def set_waypoint_order(self, order):
        self.waypoint_order= order

    def get_waypoint_order(self):
        return self.waypoint_order

    def get_place(self):
        return self.place
    
    def get_start (self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_half_hour_span(self):
        return self.half_hour_span

    
    def to_string(self):
        return self.get_place() +" "+ self.get_start()+" " + self.get_end_time() + " " + self.get_half_hour_span() + " " + str (self.get_waypoint_order())
    

    #caculate how many half hour in between start and end time
    #return : string
    def calculate_half_hours(self,start_time_str, end_time_str):
        start_time = int(start_time_str[:2]) * 60 + int(start_time_str[2:])
        end_time = int(end_time_str[:2]) * 60 + int(end_time_str[2:])
        delta_minutes = end_time - start_time
        half_hours = delta_minutes / 30
        return str(int(half_hours))

    
if __name__ == "__main__":

    test1=Event("uab", ["0000", "1000"])
    print(test1.to_string())