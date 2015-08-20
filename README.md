### insight-data-engineering-coding-challenge
Coding challenge for insight data engineering fellowship

##### Python version used
- 2.7.5

##### Python default libs used
- sys, time, getopt
- collections -> Counter

##### Instructions
###### For help
- bash ./help.sh
###### To run the program
- bash ./run.sh

###### Explanation
I have created a common processing file(analysis.py) for both kinds of features. try running help first.
  As soon as you run the program, 
  1. Previous collected tweets are processed (previous 2 months, 3 months or whatever).
  2. Then, program starts seeking the input file for new tweets with some sleep time (default is 0.8). You can change the sleep time or waiting time by using -t argument in run.sh based on your tweets verbosity.
  3. As the tweet arrives, program process that tweet and updates output files.

Obviously, processing can be improved for bounded and unbounded data, via both batch and streaming engines, we can roughly categorizing the unbounded approaches into: 
- time-agnostic
- approximation, 
- windowing by processing time, 
- and windowing by event time.

Also tools like apache storm can be used quite efficiently to apply different algorithms, for processing tweets in real time.

###### Additional: Load Test
There is a seperate folder for load test which was performed on this program. Program was tested with 2 GB data as well but due to size constraints could not be uploaded.

To run test:
- cd load_test
- bash ./test_run.sh

load_test

- test_ft1.txt => output file for first feature.
- test_ft2.txt => output file for second feature.
- test_run.sh => bash script for running this load test. 
- tweet_data_set_1.txt => Input for the test.



