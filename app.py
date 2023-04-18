from flask import Flask, request, jsonify, render_template
from utils import text_search


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def submit():

    #get all form data
    raw_datum=request.json
    name_list= raw_datum['name']
    print (name_list)


    #make api call to google map
    call=text_search.place_api()
    print("api key: ")
    api_key=input()
    result= call.api_text_search_list(name_list, api_key, '50')
    print(result)

    

    return "success"





if __name__ == '__main__':
    app.run(port=5000, debug=True,host= '0.0.0.0')