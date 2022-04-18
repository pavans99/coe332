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

Pull down the git repository in the k8 shell and enter the directory /coe332/homework06. Start all the pods, PVCs, and services with the command
	
	kubectl apply -f <filename>.yml

Repeat the command for each .yml file, replacing <filename> with the name of the file. Run the command

	kubectl get services
Record the IP addresses for the Flask and Redis services. 

Find the name of the debug deployment using the command
	
	kubectl get pods
	
The name of the pod will have a form similar to deployment-python-debug-XXXXXXXX. Enter the debug deployment using the command
	
	kubectl exec -it <pod_name> -- /bin/bash

Now one can make curl requests as described in the following section.


<h3>Making curl Requests to the Server</h3>
At this point it is important to note that the IP address of the Redis server changes sometimes. This can cause complications since the Redis server IP address is hardcoded into app.py. To make sure the correct IP address is being used one must edit app.py in a separate terminal that also contains the repository. Line 11 of app.py is shown:
	
	rd = redis.Redis(host=''10.103.4.36'', port=6379)

The value of host must be changed to the IP address of the Redis service recorded earlier. Then the Flask application must be built and pushed to Docker Hub. Having to change app.py is not preferred, but I do not know a way to reference the correct IP address directly. Now go back to the debug shell in the other terminal. 

The flask application has a few routes. To download the data to the Redis server, the POST route is used as follows:
	
	curl -X POST <FlaskIP>:5000/data
	
In this curl command and all other curl commands the value <FlaskIP> must be changed to the Flask service IP address recorded earlier. To access all the meteorite data, run the command:
	
	curl <FlaskIP>:5000/data

To access the data from a starting index run:
	
	curl <FlaskIP>:5000/data/?start=XXX

Where XXX is the starting index provided by the user. 
<h3>Example Outputs</h3>
If data is successfully read using the POST request, then the following message will be printed to the terminal:
	
	Data read

An example output to the command: 
	
	curl <FlaskIP>:5000/data/?start=295

Would be:
	
	{'name': 'Jo', 'id': '10296', 'recclass': 'EH4', 'mass (g)': '2554', 'reclat': '24.4095', 'reclong': '-15.7901', 'GeoLocation': '(24.4095, -15.7901)'}
	{'name': 'Thomas', 'id': '10297', 'recclass': 'H6', 'mass (g)': '8670', 'reclat': '-60.7340', 'reclong': '54.3187', 'GeoLocation': '(-60.7340, 54.3187)'}
	{'name': 'Agnes', 'id': '10298', 'recclass': 'H6', 'mass (g)': '801', 'reclat': '-61.5820', 'reclong': '-10.3998', 'GeoLocation': '(-61.5820, -10.3998)'}
	{'name': 'Jennifer', 'id': '10299', 'recclass': 'L5', 'mass (g)': '539', 'reclat': '-84.0579', 'reclong': '69.9994', 'GeoLocation': '(-84.0579, 69.9994)'}
	{'name': 'Christina', 'id': '10300', 'recclass': 'H5', 'mass (g)': '4291', 'reclat': '-38.1533', 'reclong': '-46.7127', 'GeoLocation': '(-38.1533, -46.7127)'}

Each line is list of a meteorite's data. The list contains parameters, such as the name of who discovered it, the mass, the class, and the location. The list is organized in order of key-value pairs. The route to return all the data looks similar but has many more entries.



