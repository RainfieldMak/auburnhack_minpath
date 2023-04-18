import requests, json, sys
  

class place_api:

    

# using  text search api call to return a set of places based on a string
# Return type : Dictionary
    def text_searh_api_call(self,query, api_key, radius):

        result_list=[]
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        query=query
        radius=radius

        # make api call
        r = requests.get(url + 'query=' + query+ 
                             '&radius' + radius+
                            '&key=' + api_key)

        #store as json
        datum= r.json()

        temp = datum['results']
        

        # keep looping upto length of y
      #  for i in range(len(temp)):
           # result.append(temp[i]['name'])
            #result_dict[temp[i]['name']]=[temp[i]['geometry']['location']['lat'],temp[i]['geometry']['location']['lng']]
       #     temp_dict={"lat":temp[i]['geometry']['location']['lat'], "lng":temp[i]['geometry']['location']['lng'], "placeName":temp[i]['name']}
        #    result_list.append(temp_dict)
        
        #result=json.dumps(result_list)



        
        return {"lat":temp[0]['geometry']['location']['lat'], "lng":temp[0]['geometry']['location']['lng'], "placeName":temp[0]['name']}


    # take an input list and return  a string object which contain the start , end , waypoint 
    #example 
    #input_list: ['uab', 'HKU','orlando disney']
    #output (str):
   # {"start": {"lat": 33.5020323, "lng": -86.80574949999999, "placeName": "University of Alabama at Birmingham"}, 
    # "end": {"lat": 22.2830891, "lng": 114.1365621, "placeName": "The University of Hong Kong"}, 
    # "waypoint": [{"lat": 28.3705684, "lng": -81.51935879999999, "placeName": "Disney Springs"}]}
    
    def api_text_search_list(self, input_list,api_key,radius):

        #longer list equal more computation needed , google map inpout max =25 (for min length path)
        if (len (input_list) > 10):
            return 0
        else:
            waypoint_list=[]
            result_dict={"start": 0, "end":0, "waypoint":[]}
            #for item in input_list:

             #   result_list.append(self.text_searh_api_call(item, api_key, radius))

            for i in  range(len(input_list)):
                
                #result_dict['start']
                if (i==0):
                    result_dict['start']= self.text_searh_api_call(input_list[i], api_key, radius)

                #result_dict['end']
                elif ( i==1): 
                     result_dict['end']= self.text_searh_api_call(input_list[i], api_key, radius)

                #result_dict['end']
                elif(i>1 and i < 11):
                     waypoint_list.append(self.text_searh_api_call(input_list[i], api_key, radius))
                else:
                    sys.stderr.write("Error: Invalid <i> , <i>  > 11 or <i> < 1?\n")
                    break

            #get list for waypoint        
            result_dict['waypoint']= waypoint_list 


        #return  a string object that contains the JSON-formatted data,      
        return json.dumps(result_dict)
    

if __name__ == "__main__":

    
    query_list=['uab', 'HKU','orlando disney']
    print ("Api : key")
    api_key = input()
    print( query_list)
    call=place_api()
    radius="50"
    result= call.api_text_search_list(query_list, api_key, radius)
    print(type(result))
    print (result)






