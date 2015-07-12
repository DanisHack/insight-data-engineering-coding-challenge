### insight-data-engineering-coding-challenge
Coding challenge for insight data engineering fellowship

##### Python version used
- 2.7.5

##### Python default libs used
- sys, time, getopt
- collections -> Counter

##### Instructions
###### For help
bash ./help.sh
###### To run the program
bash ./run.sh

###### Explanation
I have created a common processing file(analysis.py) for both kinds of features. try running help first.
  As soon as you run the program, 
  1. Previous collected tweets are processed (previous 2 months, 3 months or whatever).
  2. Then, program starts seeking the input file for new tweets with some sleep time (default is 0.8). You can change the sleep time or waiting time by using -t argument in run.sh based on your tweets verbosity.
  3. As the tweet arrives, program process that tweet and updates output files.


