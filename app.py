from flask import Flask, request, jsonify, render_template,redirect,url_for,session
from utils import text_search
import json


app = Flask(__name__)

#future recomandation , retrived 
# from a file or scrip to gnereal long 64bit random key
app.secret_key = "your-secret-key-hereasdbfwerwdsfsadd"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit",methods=["POST"])
def submit():

    #get all form data
    start = request.form["start"]
    end = request.form["end"]
    waypoints = request.form.getlist("waypoints[]")

    name_list=[start] + [end]+ waypoints 


    #make api call to google map
    call=text_search.place_api()
    print("api key: ")
    api_key=input()
    result= call.api_text_search_list(name_list, api_key, "50")
    print(result)

   # session["api_search_result"]=result

    

    return redirect(url_for("show_locations", result=result))

@app.route("/show_locations", methods=["POST", "GET"])
def show_locations():
 
    result = request.args.get ("result")
    print("From show locaitons\n")
    print (result)

    result_=json.dumps(result)
    return render_template("result.html", result =result_)



if __name__ == "__main__":
    app.run(port=5000, debug=True,host= "0.0.0.0")