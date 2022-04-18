<h1>Deploying Flask and Redis Servers to Kubernetes Cloud </h1>
The objective of this assignment is to deploy the flask application built in Homework 5 to the Kubernetes cloud. The python code, Dockerfile, and Makefile are the same files used in the Homework 5. The only new files are the .yml files.
<h2>Functions in app.py</h2>
<h3>read_data</h3>
This function reads the meteorite data to the Redis server.  
<h3>print_data</h3>
This function prints the meteorite data in json list form to the terminal with data for each meteorite on one line.   
<h3>start_data</h3>
This function prints the meteorite data in the same format as print_data but from a starting index specified in the URL. If a non-integer is passed as the start value, it will be rounded to the nearest integer. If the passed index is out of the data range, a message will be printed saying this.
<h2>Instructions for Running</h2>
<h3>Running the Application on Kubernetes</h3>
First one must ssh onto a k8 cluster using the command 

	ssh <username>@coe332-k8s.tacc.utexas.edu

Start all the pods, PVCs, and services with the command
	
	kubectl apply -f <filename>.yml

Repeat the command for each .yml file, replacing <filename> with the name of the file. Find the name of the debug deployment using the command

<h3>Making curl Requests to the Server</h3>
The flask application has few routes. To download the data to the Redis server, the POST route is used as follows:
	
	curl -X POST localhost:5030/data
	
To access all the meteorite data, run the command:
	
	curl localhost:5030/data

To access the data from a starting index run:
	
	curl localhost:5030/data/?start=XXX

Where XXX is the starting index provided by the user. 
<h3>Example Outputs</h3>
If data is successfully read using the POST request, then the following message will be printed to the terminal:
	
	Data read

An example output to the command: 
	
	curl localhost:5030/data/?start=295

Would be:
	
	{'name': 'Jo', 'id': '10296', 'recclass': 'EH4', 'mass (g)': '2554', 'reclat': '24.4095', 'reclong': '-15.7901', 'GeoLocation': '(24.4095, -15.7901)'}
	{'name': 'Thomas', 'id': '10297', 'recclass': 'H6', 'mass (g)': '8670', 'reclat': '-60.7340', 'reclong': '54.3187', 'GeoLocation': '(-60.7340, 54.3187)'}
	{'name': 'Agnes', 'id': '10298', 'recclass': 'H6', 'mass (g)': '801', 'reclat': '-61.5820', 'reclong': '-10.3998', 'GeoLocation': '(-61.5820, -10.3998)'}
	{'name': 'Jennifer', 'id': '10299', 'recclass': 'L5', 'mass (g)': '539', 'reclat': '-84.0579', 'reclong': '69.9994', 'GeoLocation': '(-84.0579, 69.9994)'}
	{'name': 'Christina', 'id': '10300', 'recclass': 'H5', 'mass (g)': '4291', 'reclat': '-38.1533', 'reclong': '-46.7127', 'GeoLocation': '(-38.1533, -46.7127)'}

Each line is list of a meteorite's data. The list contains parameters, such as the name of who discovered it, the mass, the class, and the location. The list is organized in order of key-value pairs. The route to return all the data looks similar but has many more entries.



