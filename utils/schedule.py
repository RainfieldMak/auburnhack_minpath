from utils import event
#import event


class schedule: 
    def __init__(self,result, time_list):
        #result : is in a form of dict , example, value for waypoint could be empty list
            # {"start": {"lat": 33.5020323, "lng": -86.80574949999999, "placeName": "University of Alabama at Birmingham"}, 
                # "end": {"lat": 22.2830891, "lng": 114.1365621, "placeName": "The University of Hong Kong"}, 
                # "waypoint": [{"lat": 28.3705684, "lng": -81.51935879999999, "placeName": "Disney Springs"}]}
    
        #time_list : lst of sting of time in 24hour format, example 
            #["0000", "0100", "2300", "2400" ,"1700", "1900"]
            #format:    
                # 1. total no of items will be in even number, even: start time , odd: end time
                #2. first two item will alwasy be the start and end time of starting place
                #3. third and fourth item alwasy be the start and end time of ending place
                #4. if fourth and fifth item ... exist, will always be the start and end time of waypoint(s)

        #start: event object , store the place name ,start and end time
        #end : event object , store the place name ,start and end time
        #waypoint: list ,of event object , store the place name ,start and end time of each event(waypoint)
        
        i=0        
        waypoints=[]
        self.start= event.Event(result['start']["placeName"],time_list[0])
        self.end= event.Event(result['end']["placeName"],time_list[1])

      
        if result["waypoint"] is not None:
            while (i< len(result["waypoint"])):
                waypoints.append( event.Event(result["waypoint"][i]["placeName"], time_list[i+2]))
                i+=1
        else:
            self.waypoint= None

        self.waypoint= waypoints

    def get_start(self):
        return self.start

        
    def get_end(self):
        return self.end
    
    def get_waypoints(self):

        
        if self.waypoint is not None:
            

            return self.waypoint
        else:
            return None



  


    
if __name__ == "__main__":

    test1= {"start": {"lat": 33.5020323, "lng": -86.80574949999999, "placeName": "University of Alabama at Birmingham"}, 
                 "end": {"lat": 22.2830891, "lng": 114.1365621, "placeName": "The University of Hong Kong"}, 
                 "waypoint": [{"lat": 28.3705684, "lng": -81.51935879999999, "placeName": "Disney Springs"}, 
                              {"lat": 28.3705684, "lng": -81.51935879999999, "placeName": "UAB rect"}]}
    
    time_list=[["0000" ,"0100"], ["0200", "0300"],["0400","0600"], ["0500","0700"]]


    s=schedule(test1,time_list)
    print(s.get_start().to_string())
    print(s.get_end().to_string())
    print(s.get_waypoints())