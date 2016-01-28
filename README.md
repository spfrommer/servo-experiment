*If you have not yet read the accompanying paper, please have a look at paper.pdf. The data will be hard to understand without it.*

*To read how this project came about, see [my blog post](http://sam.pfrommer.us/relationships-between-current-angular-velocity-and-torque-in-position-controlled-servos).*

### Raw and Processed Data
Raw readings collected from the Arduino are available in the "raw" folder, named as raw(weight-in-grams).txt. Each file contains the data for one complete trial, including all three forward and reverse runs. After finishing each forward run, the Arduino prints out a line indicating that it is now going to begin the return run to reposition the servo at the starting position. When it accomplishes this it prints "DONE POSITIONING" and starts the next forward revolution, if it is not already finished with all three runs.

The "processed" readings contain the time stamp in milliseconds (zero being the first reading), the position in degrees, and the current in amps divided into three columns. The data has also been parsed into six files, one for each run of a given load. These are denoted using the naming convention "processed(weight-in-grams)-(run-number).txt."

### Graphs
The data gathered in this experiment has been summarized with a number of graphs (available under "graphs" and "analysis/graphs"). The graphs for individual runs are named "run(weight-in-grams)-(run-number).pdf," correspoding to their "processed" file counterparts. The run numbers range from zero to five, representing the three forward turns and three backward turns for each trial. Runs 0, 2, and 4 are the forward revolutions at maximum speed, whereas runs 1, 3, and 5 are the reverse revolutions for durations of approximately *t*=1, 3, and 5 seconds, respectively. The runs for the 750g trials are incomplete due to the servo stalling.

For each run, the angular position and current are plotted against time. The position and current are calculated from the raw data using the formulas presented in the "Processing Data" section of the paper. A linear regression was performed for the constant velocity portion of the position plots, and a horizontal fit for the current in the same domain.

The "runsetpos-(run-number).pdf" files summarize the angle-time curves for all the different weights associated with each run. For example, the runsetpos2 file would plot all the curves from the "run(weight)-2.pdf" files on the same graph. The "runsetcur-(run-number).pdf" files are similar, but only graph the currents for the 0, 250, 500, and 700 gram runs. The slope of the position and the mean of the current was then plotted against the torque τ in "runset(runset)analysis.png."
