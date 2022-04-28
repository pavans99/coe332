<h1>Midterm Flask API Routes Flowchart</h1>
The flowchart describes the various API routes of the Flask application built in the Midterm. 

<h2>Meaning of the Shapes</h2>
The flowchart has three different shapes to specify the action taking place. Ovals indicate a request, rectangles indicate the output of a GET request, and the rhombus indicates the result of a POST request. The output of a GET request is data or informational text printed to the terminal. The output of a POST request is the downloading and reading of data, which has no visible output to the user except for a short message confirming the data has been downloaded and read. 

<h2>Organization</h2>
The flowchart follows a pattern of describing a request that can be made to the application and then describing the result of the request. Some routes have branching paths, meaning that different data will be returned depending on user input to the route. For example in the ISS Positional data, one can return a list of all the epochs if one queries the epoch route with no specifiers. However, if the user specifies a particular epoch when querying the epoch route then only data for that epoch is printed. These choices are represented by branching paths on the flowchart. 
