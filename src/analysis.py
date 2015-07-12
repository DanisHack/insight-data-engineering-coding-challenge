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
		print sum(self.unique_words_count_in_a_tweet)/float(len(self.unique_words_count_in_a_tweet))
		self.medians_unique.append(sum(self.unique_words_count_in_a_tweet)/float(len(self.unique_words_count_in_a_tweet)))

	'''
		function to calculate unique words count 
	'''
	def calculate_unique_words_in_a_tweet(self, line):
		word_list = line.split(' ')
		unique_words_count_dict = Counter(word_list)
		print unique_words_count_dict, len(unique_words_count_dict.keys())
		unique_words_count = len(unique_words_count_dict.keys())
		self.unique_words_count_in_a_tweet.append(unique_words_count)
		self.words_tweeted = self.words_tweeted + unique_words_count_dict
		

	'''
		function to each line in from tweets.txt
	'''
	def process_line(self, line):
		self.calculate_unique_words_in_a_tweet(line)
		self.calculate_median()

		print self.medians_unique


def main(argv, tweet_analysis):

	INPUT_FILE = ''
   	OUTPUT_WORDS_FILE = ''
   	OUTPUT_MEDIAN_FILE = ''

   	tweet_analysis = tweet_analysis()

   	try:
   		opts, args = getopt.getopt(argv,"hi:w:m:",["infile=","out1file=", "out2file="])
   	except getopt.GetoptError:
   		print 'test.py -i <inputfile> -w <outputfile 1> -m <outputfile 2>'
   		sys.exit(2)

   	for opt, arg in opts:
   		if opt == '-h':
   			print 'test.py -i <inputfile> -w <outputfile 1> -m <outputfile 2>'
   			sys.exit()
   		elif opt in ("-i", "--infile"):
   			INPUT_FILE = arg
   		elif opt in ("-w", "--out1file"):
   			OUTPUT_WORDS_FILE = arg
   		elif opt in ("-m", "--out2file"):
   			OUTPUT_MEDIAN_FILE = arg

   	print 'Input file is "', INPUT_FILE
   	print 'Output file 1 is "', OUTPUT_WORDS_FILE
   	print 'Output file 2 is "', OUTPUT_MEDIAN_FILE

	input_file = open(INPUT_FILE, 'r')
	input_file.seek(0,0)

	write_to_files = 0

	while True:
		line = input_file.readline()
		if not line:
			print "------- Waiting for new tweet -------"

			if write_to_files == 0:
				ft1 = open(OUTPUT_WORDS_FILE, 'w')
				ft2 = open(OUTPUT_MEDIAN_FILE, 'w')

				for key, value in sorted(tweet_analysis.words_tweeted.items()):
					ft1.write("%-50s %s %s"%(str(key),str(value),"\n"))
				ft1.close()

				ft2.seek(0,2)
				for elem in tweet_analysis.medians_unique:
					ft2.write(str(elem)+"\n")
				ft2.close()

				write_to_files = 1
				tweet_analysis.medians_unique = list()
				time.sleep(0.1)
				continue
		else:
			write_to_files = 0
			line = line.rstrip('\n')
			tweet_analysis.process_line(line)


if __name__ == '__main__':
	main(sys.argv[1:], tweet_analysis)