from flask import Flask, request
import json
import redis
import requests



app = Flask(__name__)
mdata ={}

rd = redis.Redis(host='172.17.0.13', port=6379)
k=0
z=[]
@app.route('/data', methods=['POST'])
def read_data()->str:
    """
    Downloads meteorite data to redis server.
    Args:
        None
    Returns:
        result(string): string confirming that data has been read
    """
    url = 'https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json'
    r = requests.get(url,allow_redirects=True)
    data=open('meteorite_data.json','wb').write(r.content)
    with open('meteorite_data.json','r') as f:
        x=json.load(f)
        for i in range(len(x["meteorite_landings"])):
            z.append(str(i))
            rd.set(str(i),json.dumps(x["meteorite_landings"][i]))
    k=12345 
    return "Data read \n"

@app.route('/data',methods=['GET'])
def print_data()->str:
    """
    Prints meteorite data to terminal in json list format
    Args:
        None
    Returns:
        result(string): string of meteorite data with one meteorite entry on each line
    """ 
    y=[]
    for i in range(len(z)):
        y.append(str(json.loads(rd.get(z[i]))))
    return 'Meteorite data:\n' +'\n'.join(y) +'\n'

@app.route('/data/',methods=['GET'])

def start_data()->str: 
    """
    Prints meteorite data starting from specified start point
    Args:
        start: specifies start point
    Returns:
        result(string): Prints meteorite data from specified starting point. If index is out of range, then a message is printed saying this.
    """
  
    start = int(float(request.args.get('start')))
    y=[]
    if(start<len(z)):
        for i in range(start,len(z)):
            y.append(str(json.loads(rd.get(z[i]))))
        return 'Meteorite data:\n' +'\n'.join(y) +'\n'
    else:
        return "Index out of range\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
