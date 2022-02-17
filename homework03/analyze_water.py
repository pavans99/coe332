import math
import numpy as np
import json, requests
import os.path
import logging
def turbidity_calc(a0:float,I90:float)->float:
    """
    Calculates water turbidity.
    
    Multiplies calibration constant by detector current as in Equation 1. Returns water turbidity.
    Args:
        a0 : float value equal to the calibration constant
        I90 : float value equal to the detector current
    Returns:
        T (float): water turbidity
    Raises:
        TypeError: float() argument must be a string or a number     
    """
    T = a0*I90
    return float(T)
def min_time(T0:float,d:float)->float:
    """
    Calcualtes time until water is safe.

    Uses Equation 2 and given water turbidity and decay factor to calculate time until water turbidity is below the safety threshold. Returns time in hours.
    Args:
        T : float value equal to water turbidity
        d : float value equal to decay factor per hour expressed as a decimal
    Returns
        b : float value equal to time in hours until water turbidity is below the safety threshold
    Raises:
        OverflowError: (34, 'Numerical result out of range')
    """
    Ts = T0;
    b=0
    while abs(Ts)>1:
        b=b+.01
        Ts = T0*(1-d)**b
    return float(b)
def main():
    d=.02
    data = json.loads(requests.get("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json").text)
    with open('turbidity_data.json', 'w') as out:
        json.dump(data,out,indent=2)
    with open('turbidity_data.json','r') as f:
        x=json.load(f)
        y = len(x['turbidity_data'])
        avg=0;
        for i in range(len(x['turbidity_data'])-5,len(x['turbidity_data'])):

        # travel[0] = (calc_gcd(16,82,float(x['sites'][0]['latitude']),float(x['sites'][0]['longitude'])))/10
            avg= avg+ turbidity_calc(x['turbidity_data'][i]['calibration_constant'],x['turbidity_data'][i]['detector_current'])
            #print(x['turbidity_data'][i]['detector_current'])
            #print(x['turbidity_data'][i]['calibration_constant'])
        avg=avg/5
        time = round(min_time(avg,d),2)
        logging.basicConfig(level=logging.DEBUG)
        if avg>1:
            print('Average turbidity based on last five measurements =',avg,'NTU')
            #print('Warning: Turbidity is above threshold for safe use')
            logging.warning('Turbidity is above threshold for safe use')
            print('Minimum time required to return below a safe threshold =',time,'hours')
        if avg<=1:
            print('Average turbidity based on last five measurements =',avg,'NTU')
            logging.info('Turbidity is below threshold for safe use')
            print('Minimum time required to return below a safe threshold =',time,' hours')
            
if __name__ == '__main__':
        main()
