from analyze_water import turbidity_calc, min_time,main
import numpy as np
import pytest

def test_turbidity_calc():
    assert np.round(turbidity_calc(1.1,1.1),2) == 1.21
    assert np.round(turbidity_calc(1.1,.5),2) == 0.55
    with pytest.raises(TypeError):
        turbidity_calc(4)
    with pytest.raises(ValueError):
        turbidity_calc('a',4)
    with pytest.raises(NameError):
        turbidity_calc(a,'a')

def test_min_time():
    assert np.round(min_time(1.2,.02),2) == 9.03
    assert min_time(1,.02)==0
    with pytest.raises(TypeError):
        min_time('a')
    with pytest.raises(OverflowError):
        min_time(2,-2)
    with pytest.raises(NameError):
        min_time(1,a)  
pytest.main()
