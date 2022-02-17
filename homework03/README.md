<h1>Safe Water Calculator</h1>
The scripts contain functions that check the water turbidity level and the time until until the water is below the safety threshold. The scripts automatically download data from the given url and write them to a .json file. They also contain unit tests to check whether the routine runs properly and raises errors when incorrect input formats are passed to the functions. 

<h2>analyze_water.py</h2>
This script contains three functions, `turbidity_calc` and `min_time`. 
<h3>turbidity_calc</h3>
`turbidity_calc` calculates the turbidity of the water at a given time. The function takes two arguments: calibration constaint, a0, and detector current, I90. As shown in Equation 1, the function multiplies the two inputs and returns the water turbidity.
<h3>min_time</h3>
Using Equation 2, `min_time` calculates the time until the water turbidity drops below the safety threshold of 1 NTU. The function takes two arguments: T0, the initial water turbidity, and d, the decay factor per hour expressed as a decimal. 
<h3>main</h3>
main downloads the turbidity data and saves it to a file called "`turbidity_data.json`." The calibration constants and detector currents from the five most recent measurements are each averaged. These averages are passed to turbidity\_calc and the turbidity calculated is passed to `min_time`. The turbidity measurement is printed to the terminal, whether it is above or below the safety threshold, and the time required for it to reach the safety threshold.
<h2>test_analyze_water.py</h2>
This script contains 2 functions, test\_analyze\_water and test\_min\_time. Each function contains 5 unit tests for the function it is testing. 
<h3>test_turbidity_calc</h3>
Two unit tests make sure that the turbidity\_calc returns the correct values when run with proper inputs. The other 3 tests checks whether turbidity\_calc raises the correct errors when given bad inputs, such as only one input, inputs that are strings, or inputs of undefined variables.
<h3>test_min_time.py</h3>
Two unit tests make sure that the min\_time returns the correct values when run with proper inputs. The other 3 tests checks whether min\_time raises the correct errors when given bad inputs, such as only one input, inputs that are strings, or inputs of undefined variables.

<h2>How to Run the Scripts</h2>
<h3>analyze_water.py</h3>
To run this script just execute analyze\_water.py on the command line. If the "requests" library is not installed run "pip3 install --user requests" on the command line before executing. Results are printed to the terminal where they can be read. Example results are shown:<br>  
Average turbidity based on last five measurements = 1.166279 NTU<br>
WARNING:root:Turbidity is above threshold for safe use <br>
Minimum time required to return below a safe threshold = 7.62 hours <br>
<h3>test_analyze_water.py</h3>
To run this script just execute test\_analyze\_water.py on the command line. Pytest is embedded in the script, so pytest will automatically run when the script is executed. Alternatively, pytest can be run from the command line in the directory, which will return the same results. The results of pytest are printed to the terminal.
<h2>How to download the data</h2>
analyze\_water.py automatically downloads the data and writes it to a .json file. However, the "requests" library must be installed to run the script. To install "requests" run "pip3 install --user requests" on the command line.
