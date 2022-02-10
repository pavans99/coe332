import numpy as np
import json

def sitegen():
    x = np.zeros(5)
    y= x.copy()
    z= []
    comp = ['stony','iron','stony-iron']
    for i in range(5):
        x[i] = np.random.uniform(0,2)+16
        y[i] = np.random.uniform(0,2)+82
        z.append(comp[np.random.randint(3)])
    
    d={
      "sites": [
        {
          "site_id": 1,
          "latitude": x[0],
          "longitude": y[0],
          "composition": z[0]
        },
        {
          "site_id": 2,
          "latitude": x[1],
          "longitude": y[1],
          "composition": z[1]
        },
        {
          "site_id": 3,
          "latitude": x[2],
          "longitude": y[2],
          "composition": z[2]
        },
        {
          "site_id": 4,
          "latitude": x[3],
          "longitude": y[3],
          "composition": z[3]
        },
        {
          "site_id": 5,
          "latitude": x[4],
          "longitude": y[4],
          "composition": z[4]
        }
        ]}
    with open('sites.json', 'w') as out:
        json.dump(d, out, indent=2)

if __name__ == '__main__':
    sitegen()
