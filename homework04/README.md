<h1>Docker Practice</h1>
The docker image comprises two scripts and one .ijson file with data. ml_data_analysis.py is the main script and contains the functions compute_average_mass, check_hemisphere, count_classes, and main. Main prints out summary data produced by the other three functions using data from the .json file. The second script, test_ml_data_analysis.py, contains unit tests for all functions besides main. The purpose of the assignment is to containerize the scripts so that anyone can run them if they download the docker iamge file. All code dependencies are built into the image.
<h2>Functions</h2>
<h3>compute_average_mass</h3>
This function is relatively simple. The function accepts a list of dictionaries containing meteorite data. The mean mass of the meteorites is computed and returned. 
<h3>check_hemisphere</h3>
This function is also simple. The function accepts coordinates of latitude and longitude. If the latitude is positive then the meteorite lies in the northern hemisphere and if negative in the southern hemisphere. If the longitude is positve then the meteorite lies in the eastern hemisphere and if negative in the western hemisphere. If the latitude or longitude is 0 then a ValueError is raised. The output is a combination of northern or southern and eastern or western hemispheres. 
<h3>count_classes</h3>
This function accepts a list of dictionaries of meteorite data. The number of meteors in each class is counted and returned in the form of a dictionary of class counts.
<h3>main</h3>
main accepts user input for meteorite data. The meteorite data must be in .json file and contain a list of dictionaries of meteorite data in the format specified by the sample data in the given .json file. An example of the proper format is shown below.
```
	{
	 "name": "Ruiz",
	 "id": "10001",
 	 "recclass": "L5",
	 "mass (g)": "21",
	 "reclat": "50.775",
	 "reclong": "6.08333",
	 "GeoLocation": "(50.775, 6.08333)"
	 }

```

The other three functions process the input data, and main prints out summary data. Example summary data is shown below.

	Average mass of 30 meteor(s): 83857.3 grams

	Hemisphere summary data:
	There were 21  meteors found in the Northern & Eastern quadrant
	There were 6  meteors found in the Northern & Western quadrant
	There were 0  meteors found in the Southern & Eastern quadrant
	There were 3  meteors found in the Southern & Western quadrant

	Class summary data:
	The L5 class was found 1 times
	The H6 class was found 1 times
	The EH4 class was found 2 times
	The Acapulcoite class was found 1 times
	The L6 class was found 6 times
	The LL3-6 class was found 1 times
	The H5 class was found 3 times
	The L class was found 2 times
	The Diogenite-pm class was found 1 times
	The Stone-uncl class was found 1 times
	The H4 class was found 2 times
	The H class was found 1 times
	The Iron-IVA class was found 1 times
	The CR2-an class was found 1 times
	The LL5 class was found 2 times
	The CI1 class was found 1 times
	The L/LL4 class was found 1 times
	The Eucrite-mmict class was found 1 times
	The CV3 class was found 1 times



<h2>Instructions for Running</h2>
<h4>Pulling the Image</h4>
The image is pulled using one command:

	git pull pavanshukla99/ml_data_analysis:hw04. 

<h4>Building the Image</h4>
Several components are needed to build the image. The Dockerfile provided on GitHub, the script ml_data_analysis.py, the script test_ml_data_analysis.py, and a .json data file in the required format are needed to build the image. test_ml_data_analysis.py will only work with the given sample data. If all the required files are present then the command:
```

	docker build -t pavanshukla99/ml_data_analysis:hw04

will run properly and build the image.

<h4>Running Using the Sample Data</h4>
To run the image using the sample data one must first pull down the image as described in the first step. Then the command:

	docker run --rm -v $PWD:/data pavanshukla99/ml_data_analysis:hw04 ml_data_analysis.py /code/Meteorite_Landings.json

will run the ml_data_analysis.py for the sample data.

<h4>Running Using User Data</h4>
The image must be pulled down first using the command given in the running using sample data step. Then the command:

	docker run --rm -v $PWD:/data pavanshukla99/ml_data_analysis:hw04 ml_data_analysis.py /data/userdata.json

where userdata.json is a placeholder, will run ml_data_analysis.py for the user's input data. 
<h4>Running the Unit Tests</h4>
To run the unit tests the image must be pulled down first. Then run the command 

	docker run --rm -v $PWD:/data pavanshukla99/ml_data_analysis:hw04 pytest code/test_ml_data_analysis.py

to execute the unit tests. The unit tests are independent of user input, as the inputs to the unit tests are specified to demonstrate certain results.


