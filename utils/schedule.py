from utils import event
#import event


class schedule: 
    def __init__(self,place_list, time_list):
        #place_list : is in a form of dict , example, value for waypoint could be empty list
            # {"start": {"lat": 33.5020323, "lng": -86.80574949999999, "placeName": "University of Alabama at Birmingham"}, 
                # "end": {"lat": 22.2830891, "lng": 114.1365621, "placeName": "The University of Hong Kong"}, 
                # "waypoint": [{"lat": 28.3705684, "lng": -81.51935879999999, "placeName": "Disney Springs"}]}
    
        #time_list : a dict 
            #{"start":["0000", "0100"],"end" :["2300", "2400"] ,"waypoint" : ["1700", "1900"]}
           

        #start: event object , store the place name ,start and end time
        #end : event object , store the place name ,start and end time
        #waypoint: list ,of event object , store the place name ,start and end time of each event(waypoint)
        
        i=0        
        waypoints=[]
        self.start= event.Event(place_list['start']["placeName"],time_list['start'])
        self.end= event.Event(place_list['end']["placeName"],time_list["end"])

      
        if place_list["waypoint"] is not None:
            while (i< len(place_list["waypoint"])):
                waypoints.append( event.Event(place_list["waypoint"][i]["placeName"], time_list["waypoint"][i]))
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
    
    time_list={"start":["0000", "0100"],"end" :["2300", "2400"] ,"waypoint" : [["1700", "1900"], ["0400", "0600"]]}


    s=schedule(test1,time_list)
    print(s.get_start().to_string())
    print(s.get_end().to_string())
    for e in s.get_waypoints():
        print(e.to_string())