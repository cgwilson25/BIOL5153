#! /usr/bin/env python3

import argparse

#Creating an argparse object
parser = argparse.ArgumentParser(description="this script will be used in the future")

#adding positional arguments for each of the variables below
parser.add_argument("gff", help="opens up gff file", type=str)
parser.add_argument("fasta", help="opens up FASTA file", type=str)
#adding optional arguments for the rest of t

#setting up args to be parsed
args = parser.parse_args()

#opens files
with open(args.gff) as x:
	#loop over all the lines in the file
	for line in x:
		 if not line.rstrip():
			continue

		 else:
			lines = line.rstrip()

	   #split line on tab character
			columns = line.split('\t')

	#give variable names to the columns
			organism = columns[0]
			source = columns[1]
			feature_type = columns[2]
			start = columns[3]
			end = columns[4]
			length = columns[5]
			strand	= columns[6]
			attributes = columns[7]

			print(attributes)
			#add the length to colunn 5
			columns[5] = int(end) - int(start) + 1

			new_line = "\t".join(columns)
			print(new_line)



#        line.strip("\n")
 #       split = line.split("\t")
  #      len = int(split[4]) - int(split[3])
   #     len += 1
    #    print(split[2], str(len))

#print('shibidy flibidy wibidy wap')

