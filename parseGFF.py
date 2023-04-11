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
g = open(args.gff_name, 'r')

for line in g:
	line.strip("\n")
	split = line.split("\t")
	len = int(split[4]) - int(split[3])
	len += 1
	print(split[2], str(len))

print('shibidy flibidy wibidy wap')

