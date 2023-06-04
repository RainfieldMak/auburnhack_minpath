from utils import event
#import event


#Note: 1/6/2023 Is it neccessary to make object, since need to convert back to dict and reorder 

class schedule: 
    def __init__(self,place_list, time_list):
        #place_list : is in a form of dict , example, value for waypoint could be empty list
            # {'1': ['UAB Hospital', '4 mins', '0.9 km'], '2': ['Hotel Indigo Birmingham Five Points S - Uab, an IHG Hotel', '4 mins', '1.1 km'], 'start': ['University of Alabama at Birmingham', '4 mins', '0.9 km'],
             # 'final': ['UAB Campus Recreation', '4 mins', '0.9 km'], 
             # 'end': 'UAB Campus Recreation'}
    
        #time_list : a dict 
            #{"start":["0000", "0100"],"end" :["2300", "2400"] ,"waypoint" : ["1700", "1900"]}
           

        #start: event object , store the place name ,start and end time
        #end : event object , store the place name ,start and end time
        #waypoint: list ,of event object , store the place name ,start and end time of each event(waypoint)
        
        i=0        
        waypoints=[]
        self.start= event.Event(place_list['start'][0],time_list['start'], -1)
        self.end= event.Event(place_list['end'],time_list["end"], -1)

      

        for key in place_list:
            if key== "start" or key == "end" or key=='final':
                continue
            else :
                waypoints.append( event.Event(place_list[key][0], time_list["waypoint"][i], i+1))
                
                i+=1



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
        
    def as_dict(self):
        dict = self.__dict__
        for key in dict:
            if key == "waypoint":
                i=0
                for item in dict[key]:
                    dict[key][i]= item.__dict__
                    i+=1
            
            else:
                dict[key]= dict[key].__dict__


        output=[]
        output.append(dict['start'])
        for item in dict['waypoint']:
            output.append(item)

        output.append(dict['end'])

        return output



  


    
if __name__ == "__main__":

    test1= {'1': ['UAB Hospital', '4 mins', '0.9 km'], '2': ['Hotel Indigo Birmingham Five Points S - Uab, an IHG Hotel', '4 mins', '1.1 km'], 'start': ['University of Alabama at Birmingham', '4 mins', '0.9 km'],
             'final': ['UAB Campus Recreation', '4 mins', '0.9 km'], 
             'end': 'UAB Campus Recreation'}
    
    time_list={"start":["0000", "0100"],"end" :["2300", "2400"] ,"waypoint" : [["1700", "1900"], ["0400", "0600"]]}


    s=schedule(test1,time_list)
    temp= s.__dict__
    print (temp)

    temp_= s.as_dict()
    print(temp_)
    print(type (s))
    e_list=[]
  