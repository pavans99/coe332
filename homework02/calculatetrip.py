import math
import numpy as np
from sitegenerator import sitegen
import json
#function for calculating distance
mars_radius = 3389.5    # km
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )
sitegen()
travel = np.zeros(5)
sample = np.zeros(5)
with open('sites.json','r') as f:
    x=json.load(f)
    travel[0] = (calc_gcd(16,82,float(x['sites'][0]['latitude']),float(x['sites'][0]['longitude'])))/10
    if(x['sites'][0]['composition']=='stony'):
        sample[0] = 1
    elif(x['sites'][0]['composition']=='iron'):
        sample[0]=2;
    elif(x['sites'][0]['composition']=='stony-iron'):
        sample[0]=3
    for i in range(1,len(x['sites'])):
        travel[i] = (calc_gcd(float(x['sites'][i-1]['latitude']),float(x['sites'][i-1]['longitude']),float(x['sites'][i]['latitude']),\
                             float(x['sites'][i]['longitude'])))/10
        if(x['sites'][i]['composition']=='stony'):
            sample[i] = 1
        elif(x['sites'][i]['composition']=='iron'):
            sample[i]=2;
        elif(x['sites'][i]['composition']=='stony-iron'):
            sample[i]=3


for i in range(len(x['sites'])):
    print('leg =',i+1,',','time to travel =', travel[i],'hr,', 'time to sample =', int(sample[i]),'hr')

print('number of legs =', i+1,', total time elapsed =', sum(travel+sample))
