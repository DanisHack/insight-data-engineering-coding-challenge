#!/usr/bin/env bash

# example of the run script for running the word count

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
python src/analysis.py -i tweet_input/tweet_input/tweets.txt -w tweet_output/tweet_output/ft1.txt -m tweet_output/tweet_output/ft2.txt
