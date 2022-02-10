<h1>Meteorite Trip Calculator</h1>
The scripts comprise a routine that generates five random meteorite sites and the time for the robot to travel to each site as well as analyze the meteorites.The site data is written to a .json file and then read from the .json file to calculate trip time. The objective of the assignment is to gain experience working with different data formats using .json files.

<h2>sitegenerator.py</h2>
This script contains a function "sitegen" that generates five random meteorites, each with a location(latitude, longitude) and composition. The script sitegenerator.py calls sitegen to generate a "sites.json" file with meteor date.

<h2>calculatetrip.py</h2>
This script calls sitegen and overwrites any existing file named "sites.json". The traveling time of each trip and time to sample the meteorite is calculated and printed for each of the five legs of the journey, and then the total trip length is printed.

<h2>calculatetrip2.py</h2>
This script is similar to calculatetrip.py, except it will not overwrite an existing "sites.json" file. If a "sites.json" file already exists, it uses that file data to calculate trip times, and if a "sites.json" file doesn't exist one is generated and then used to calculate trip times. This script can be used in conjunction with sitegenerator.py, by first running sitegenerator.py, then running calculatetrip2.py.

<h2>How to Run the Scripts<h2>
<h3>calculatetrip.py Method<h3>
To use this method simply run calculatetrip.py. Results are printed to the terminal where they can be read. New data is generated everytime the script is run.

<h3>calculatetrip2.py Method<h3>
To use this method, there are two ways. Either one can first run sitegenerator.py to generate a "sites.json" file and then run calculatetrip2.py to generate trip calculations for the "sites.json" file. The second method is to run calculatetrip2.py without running sitegenerator.py, in which case calculatetrip2.py will generate its own "sites.json" file if one does not already exist and perform trip calculations on this data.
