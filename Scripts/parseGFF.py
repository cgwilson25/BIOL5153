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

# print bash header
gff_file = open(args.gff, "r")
fasta_file = open(args.fasta, "r")

#what was supposed to be done
#with open(args.gff) as x:
#       for line in x:
#               print(line)
