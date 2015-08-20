import sys, time, getopt
from collections import Counter


class tweet_analysis:
	words_tweeted = Counter({})
	medians_unique = list()
	unique_words_count_in_a_tweet = list()

	'''
		function to calculate median and append into medians_unique 
	'''
	def calculate_median(self):
		#print sum(self.unique_words_count_in_a_tweet)/float(len(self.unique_words_count_in_a_tweet))
		self.medians_unique.append(sum(self.unique_words_count_in_a_tweet)/float(len(self.unique_words_count_in_a_tweet)))

	'''
		function to calculate unique words count 
	'''
	def calculate_unique_words_in_a_tweet(self, line):
		word_list = line.split(' ')

		# remove double spaces
		word_list = filter(None, word_list)
		print word_list

		unique_words_count_dict = Counter(word_list)
		#print unique_words_count_dict, len(unique_words_count_dict.keys())
		unique_words_count = len(unique_words_count_dict.keys())
		self.unique_words_count_in_a_tweet.append(unique_words_count)
		self.words_tweeted = self.words_tweeted + unique_words_count_dict
		

	'''
		function to process each line in from tweets.txt
	'''
	def process_line(self, line):
		self.calculate_unique_words_in_a_tweet(line)
		self.calculate_median()

		#print self.medians_unique


def main(argv, tweet_analysis):

	INPUT_FILE = ''
   	OUTPUT_WORDS_FILE = ''
   	OUTPUT_MEDIAN_FILE = ''
   	SLEEP_TIME = ''

   	tweet_analysis = tweet_analysis()

   	try:
   		opts, args = getopt.getopt(argv,"ht:i:w:m:",["stime=","infile=","out1file=", "out2file="])
   	except getopt.GetoptError:
   		print '\ncommand:\npython <filename> <options>\n'
   		print '\nExample usage:\npython test.py -t <sleeptime> -i <inputfile> -w <outputfile 1> -m <outputfile 2>\n\nOptions:\n'
   		print '-t : waiting time or sleep time.\n\tif verbosity of tweets is low, try increasing increasing sleep time using this argument.\n\tIf you do not specify this, Default sleep time is 0.8.\n-i : input file path, without quotes\n-w : output file path for first feature (words_tweeted), without quotes\n-m : output file path for second feature (median_unique), without quotes\n'
   		sys.exit(2)

   	for opt, arg in opts:
   		if opt == '-h':
   			print '\ncommand:\npython <filename> <options>\n'
   			print '\nExample usage:\npython test.py -t <sleeptime> -i <inputfile> -w <outputfile 1> -m <outputfile 2>\n\nOptions:\n'
   			print '-t : waiting time or sleep time.\n\tif verbosity of tweets is low, try increasing increasing sleep time using this argument.\n\tIf you do not specify this, Default sleep time is 0.8.\n-i : input file path, without quotes\n-w : output file path for first feature (words_tweeted), without quotes\n-m : output file path for second feature (median_unique), without quotes\n'
   			sys.exit()
   		elif opt in ("-t", "--stime"):
   			SLEEP_TIME = arg
   		elif opt in ("-i", "--infile"):
   			INPUT_FILE = arg
   		elif opt in ("-w", "--out1file"):
   			OUTPUT_WORDS_FILE = arg
   		elif opt in ("-m", "--out2file"):
   			OUTPUT_MEDIAN_FILE = arg

   	if SLEEP_TIME:
   		print 'Sleep time is "', SLEEP_TIME, type(SLEEP_TIME), int(SLEEP_TIME)

   	print 'Input file is "', INPUT_FILE
   	print 'Output file 1 is "', OUTPUT_WORDS_FILE
   	print 'Output file 2 is "', OUTPUT_MEDIAN_FILE

	input_file = open(INPUT_FILE, 'r')
	input_file.seek(0,0)

	write_to_files = 0

	while True:
		line = input_file.readline()
		if not line:

			if write_to_files == 0:
				ft1 = open(OUTPUT_WORDS_FILE, 'w')
				ft2 = open(OUTPUT_MEDIAN_FILE, 'w')

				for key, value in sorted(tweet_analysis.words_tweeted.items()):
					ft1.write("%-50s %s %s"%(str(key),str(value),"\n"))
				ft1.close()

				ft2.write('\n'.join(map(str, tweet_analysis.medians_unique)))
				ft2.close()

				write_to_files = 1
				print "\n#### Tweets in input file processed, Check %s and %s  ####\n"%(OUTPUT_WORDS_FILE, OUTPUT_MEDIAN_FILE)
				continue
			else:

				print "------- Waiting for new tweet to come -------\n"
				if SLEEP_TIME:
					time.sleep(int(SLEEP_TIME))
				else:
					#print SLEEP_TIME
					time.sleep(0.1)
		else:
			write_to_files = 0
			line = line.rstrip('\n')
			tweet_analysis.process_line(line)


if __name__ == '__main__':
	main(sys.argv[1:], tweet_analysis)
