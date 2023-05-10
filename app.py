from flask import Flask, request, jsonify, render_template,redirect,url_for,session,flash,sessions
from utils import text_search , schedule, event
import json
import ast


app = Flask(__name__)

#future recomandation , retrived 
# from a file or scrip to gnereal long 64bit random key
app.secret_key = "your-secret-key-hereasdbfwerwdsfsadd"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit",methods=["POST"])
def submit():

    i =0

    #get all form data
    start = request.form["start"]
    end = request.form["end"]
    time_list= request.form.getlist("time-range")
    waypoints = request.form.getlist("waypoints[]")
    name_list=[start] + [end]+ waypoints 


    #if nothing being input in the waypoint , delete last two item in list 
    if len(waypoints[0]) == 0:
        time_list.pop(-1)
        time_list.pop(-1)

    print(time_list)

    #make the start and end time into a tuple and store into a new list
    #new_time= [time_list[i:i+2] for i in range(0, len(time_list), 2)]

    while i < len(time_list) -1:

        #end time earlier than start time case
        if int (time_list[i])> int (time_list[i+1]):
            flash("end time cannot earlier than start time")
            return redirect(url_for("index"))
        else:
            i=i+2

    #make api call to google map
    call=text_search.place_api()
    print("api key: ")
    api_key=input()
    result= call.api_text_search_list(name_list, api_key, "50")
    print(result)

   # session["api_search_result"]=result

    

    return redirect(url_for("show_locations", result=result , time_list=time_list))

@app.route("/show_locations", methods=["POST", "GET"])
def show_locations():
 
    #get data from sbmit()
    result = request.args.get ("result")
    time_list = request.args.getlist ("time_list")


    #make the start and end time into a tuple and store into a new list
    new_time_list= [time_list[i:i+2] for i in range(0, len(time_list), 2)]

    #convert it into dict , the correct format use in schedule object 
    new_time_dict = {"start":new_time_list[0] , "end": new_time_list[1], "waypoint": new_time_list[2::]}


    #convert result(string) to dict 
    place_dict = ast.literal_eval(result)
    print(type (place_dict))
    print (place_dict) 
    print( new_time_dict)


    #save into session data
    session["place_list"]=place_dict
    session["time_list"]=  new_time_dict


    #delay converting !!! 10 May , so to pass to html and then create itneray     
    itneray=schedule.schedule(place_dict,  new_time_dict)

    #sanity check
    print (itneray.get_start().to_string())
    print (itneray.get_end().to_string())
    for e in itneray.get_waypoints():
        print(e.to_string())



    #conver to json format
    result_=json.dumps(result)
    return render_template("result.html", result =result_)



if __name__ == "__main__":
    app.run(port=5000, debug=True,host= "0.0.0.0")