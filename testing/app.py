from flask import Flask, request
import json
import redis
import requests
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)
mdata ={}

#rd = redis.Redis(host='172.17.0.13', port=6379)
rd = redis.Redis(host='10.103.4.36',port=6379)


def oe2rv(oe,mu,M):
    d2r=np.pi/180
    sma=oe[0]
    emag=oe[1]
    i=oe[2]*d2r
    sw=oe[3]*d2r
    bw=oe[4]*d2r
    nu= oe[5]*d2r
    rmag = sma*(1-emag**2)/(1+emag*np.cos(nu))
    r=np.array([rmag*np.cos(nu), rmag*np.sin(nu),0])
    p=sma*(1-emag**2)
    v= np.array([-np.sin(nu)*np.sqrt(mu/p), (emag +np.cos(nu))*np.sqrt(mu/p), 0])
    r1 = np.array([[np.cos(bw), -np.sin(bw), 0],[np.sin(bw), np.cos(bw), 0],[0,0,1]])
    r2 = np.array([[1,0,0],[0, np.cos(i), -np.sin(i)], [0, np.sin(i), np.cos(i)]])
    r3 = np.array([[np.cos(sw), -np.sin(sw), 0],[np.sin(sw), np.cos(sw),0],[0,0,1]])
    rotm = np.matmul(r1,r2)
    rotm = np.matmul(rotm,r3)
    rijk = rotm.dot(r)
    vijk = rotm.dot(v)
    E= np.arccos(abs(r[0]/sma))
  #print(r[0]/sma)
    M2 = E*-emag*np.sin(E)
    M2=-M2
    rcurr=np.zeros((3,1))
    err=abs(M2-M)
    rcurr[0]=rijk[0]
    rcurr[1]=rijk[1]
    rcurr[2]=rijk[2]
  
  
    return [rijk[0],rijk[1],rijk[2],vijk[0],vijk[1],vijk[2],rcurr,err]


@app.route('/data', methods=['POST'])
def read_data()->str:
    """
    Downloads meteorite data to redis server.
    Args:
        None
    Returns:
        result(string): string confirming that data has been read
    """
    url = 'https://data.nasa.gov/resource/b67r-rgxc.json'
    r = requests.get(url,allow_redirects=True)
    data=open('b67r-rgxc.json','wb').write(r.content)
    with open('b67r-rgxc.json','r') as f:
        x=json.load(f)
        for i in range(len(x)):
            z.append(str(i))
            rd.set(str(i),json.dumps(x["meteorite_landings"][i]))
    return "Data read \n"

@app.route('/plot/',methods=['GET'])

def start_data()->str: 
    """
    Prints meteorite data starting from specified start point
    Args:
        start: specifies start point
    Returns:
        result(string): Prints meteorite data from specified starting point. If index is out of range, then a message is printed saying this.
    """
  
    index = int(float(request.args.get('index')))
    d2r=180/np.pi
    with open('b67r-rgxc.json','r') as f:
        x=json.load(f)
        sma=(x[index]['q_au_1']+x[index]['q_au_2'])/2
        emag = x[index]['e']
        i = x[index]['i_deg']*d2r
        sw = x[index]['w_deg']*d2r
        bw = x[index]['node_deg']*d2r
        nu=0
        oe=[sma,emag,i,sw,bw,nu]

        au2km = 1.496*10**8
        mu=1.327*10**11
        y2m = 525600
        T=x[index]['p_yr']*y2m
        n=2*np.pi/T
        tcurr = T-x[index]['tp_tdb']+x[index]['epoch_tdb']
        M=n*(tcurr)

        k=1000
        cond=0;
        curr=[]
        tol=10**-2
        traj=[]
        rx,ry,rz,vx,vy,vz = ([] for h in range(6))
        for j in range(k):
            traj.append(oe2rv(oe,mu,M))
            rx.append(traj[j][0])
            ry.append(traj[j][1])
            rz.append(traj[j][2])
            vx.append(traj[j][3])
            vy.append(traj[j][4])
            vz.append(traj[j][5]i)
            if(rv[j][7]<tol and cond==0 and j>0):
                curr = traj[j-1][6]/au2km        
                cond=cond+1
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(rx,ry,rz,color='blue')
        ax.scatter(curr[0],curr[1],curr[2],color='red',s=150)
        ax.scatter(0,0,0,color='orange',s=200)
     
    return "Trajectory plotted \n"


@app.route('/rv/',methods=['GET'])

def rv_data()->str:
    """
    Prints meteorite data starting from specified start point
    Args:
        start: specifies start point
    Returns:
        result(string): Prints meteorite data from specified starting point. If index is out of range, then a message is printed saying this.
    """

    index = int(float(request.args.get('index')))
    d2r=180/np.pi
    with open('b67r-rgxc.json','r') as f:
        x=json.load(f)
        sma=(x[index]['q_au_1']+x[index]['q_au_2'])/2
        emag = x[index]['e']
        i = x[index]['i_deg']*d2r
        sw = x[index]['w_deg']*d2r
        bw = x[index]['node_deg']*d2r
        nu=0
        oe=[sma,emag,i,sw,bw,nu]

        au2km = 1.496*10**8
        mu=1.327*10**11
        y2m = 525600
        T=x[index]['p_yr']*y2m
        n=2*np.pi/T
        tcurr = T-x[index]['tp_tdb']+x[index]['epoch_tdb']
        M=n*(tcurr)

        k=1000
        cond=0;
        curr=[]
        tol=10**-2
        traj=[]
        rx,ry,rz,vx,vy,vz = ([] for h in range(6))
        for j in range(k):
            traj.append(oe2rv(oe,mu,M))
            rx.append(traj[j][0])
            ry.append(traj[j][1])
            rz.append(traj[j][2])
            vx.append(traj[j][3])
            vy.append(traj[j][4])
            vz.append(traj[j][5]i)
            if(rv[j][7]<tol and cond==0 and j>0):
                curr = traj[j-1][6]/au2km
                cond=cond+1

    return 'Meteorite data:\n' +'\n'.join(curr) +'\n'
 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
