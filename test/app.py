

from flask import Flask, render_template,session

app = Flask(__name__)

app.secret_key = "your-secret-key-hereasdbfwerwdsfsadd"

@app.route('/')
def index():
    locations = [{'place': 'University of Alabama at Birmingham', 'start_time': '0000', 'end_time': '0100', 'half_hour_span': '2', 'waypoint_order': -1},
                  {'place': 'UAB Hospital', 'start_time': '1700', 'end_time': '1900', 'half_hour_span': '4', 'waypoint_order': 1},
                    {'place': 'Hotel Indigo Birmingham Five Points S - Uab, an IHG Hotel', 'start_time': '0400', 'end_time': '0600', 'half_hour_span': '4', 'waypoint_order': 2}, 
                    {'place': 'UAB Campus Recreation', 'start_time': '2300', 'end_time': '2400', 'half_hour_span': '2', 'waypoint_order': -1}]
    session['locations']=locations
    
    print(session['locations'])
    print(session['locations'][0]['place'])
    return render_template('index.html')




if __name__ == "__main__":
    app.run(port=5000, debug=True,host= "0.0.0.0")
