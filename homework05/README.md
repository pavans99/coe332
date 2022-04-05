<h1>Flask Application for Reading Data To and From Redis Server </h1>
There are five files in the repository, four of which are necessary to running the application. The script app.py contains the functions and routes needed to run the application. Dockerfile contains the instructions necessary to build the image of the flask application. requirements.txt contains the required libraries needed to run app.py. Makefile builds, runs, and pushes the Docker image. Makefile is not necessary to run the application, but it is easier to run the Makefile than build the image and run the container manually.
<h2>Functions</h2>
<h3>read_data</h3>
This function reads the meteorite data to the Redis server.  
<h3>print_data</h3>
This function prints the meteorite data in json list form to the terminal with data for each meteorite on one line.   
<h3>start_data</h3>
This function prints the meteorite data in the same format as print_data but from a starting index specified in the URL. If a non-integer is passed as the start value, it will be rounded to the nearest integer. If the passed index is out of the data range, a message will be printed saying this.
<h2>Instructions for Running</h2>
<h3>Pulling and Running the Redis Server</h3>
The default redis image is pulled and the redis server is run using the commands:

	 docker pull redis:6
	 docker run -d -p 6430:6379 -v $(pwd)/data:/data --name=hw5-redis redis:6 --save 1 1

<h3>Pulling and Running the Flask Application</h3>
The Docker image is pulled and run using the commands:
	
	docker pull pavanshukla99/hw5:latest
	docker run --name "hw5" -d -p 5030:5000 pavanshukla99/hw5:latest

<h3>Building and Running the Flask Application</h3>
First the repository must be pulled from GitHub using the command:
	
	git clone https://github.com/pavans99/coe332.git

Then move into the directory coe332/homework05. At this point start the Redis server by executing the command specified in the instructions for running the Redis server. It should be noted that the Redis port may have changed. If the Redis port has changed, then the script app.py will have to be changed. To view the Redis container ID run the command:
	
	docker ps

Then find the container ID associated with the name "hw5-redis". Then run 
	
	docker inspect <contained_id> | grep IPAddress

Which will print the IP address. Line 11 of app.py is
	
	rd = redis.Redis(host='172.17.0.13', port=6379)

The argument of "host" must be changed to whatever IP address was found using "docker inspect". The IP address given is the one that I usually had, but it occasionally changed when restarting the Redis server.

At this point there are two options. One can run the command 
	
	make

which will build, run, and push the Flask application. Alternatively one can run the commands in the Makefile individually to build and run the application. The commands are 
	
	docker build -t pavanshukla99/hw5:latest .
	docker run --name "hw5" -d -p 5030:5000 pavanshukla99/hw5:latest

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


	
	
	
	





