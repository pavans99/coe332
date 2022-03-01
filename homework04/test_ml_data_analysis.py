from ml_data_analysis import compute_average_mass, count_classes, check_hemisphere
import pytest
import json
import os.path

 
def test_compute_average_mass():
    user_input = 'Meteorite_Landings.json'
    print(os.path.isfile(user_input))
    if os.path.isfile(user_input)==False:
        user_input = 'code/Meteorite_Landings.json'
    with open(user_input, 'r') as f:
        ml_data = json.load(f)
        assert compute_average_mass(ml_data['meteorite_landings'], 'mass (g)')==83857.3
        with pytest.raises(KeyError):
            compute_average_mass(ml_data['meteorite_landings'], 5)
        with pytest.raises(NameError):
            compute_average_mass(ml_data['meteorite_landings'], a) 
        with pytest.raises(TypeError):
            compute_average_mass([1,2,3,4], 'mass (g)')
        with pytest.raises(TypeError):
            compute_average_mass()
def test_check_hemisphere():
    assert check_hemisphere(1,1) == 'Northern & Eastern'
    assert check_hemisphere(-1,-1) == 'Southern & Western'
    with pytest.raises(ValueError):
        check_hemisphere(1,0)
    with pytest.raises(ValueError):
        check_hemisphere(0,1)
    with pytest.raises(NameError):
        check_hemisphere(a,10)    
def test_count_classes():
    user_input = 'Meteorite_Landings.json'
    if os.path.isfile(user_input)==False:
        user_input = 'code/Meteorite_Landings.json'
    with open(user_input, 'r') as f:
         ml_data = json.load(f)
         assert type(count_classes(ml_data['meteorite_landings'], 'recclass')) ==  dict
         with pytest.raises(KeyError):
             count_classes(ml_data['meteorite_landings'], 5)
         with pytest.raises(NameError):
             count_classes(ml_data['meteorite_landings'], a)
         with pytest.raises(TypeError):
             count_classes([1,2,3],'mass (g)')
         with pytest.raises(TypeError):
             count_classes()
pytest.main()
