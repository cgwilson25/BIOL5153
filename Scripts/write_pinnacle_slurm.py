#! /usr/bin/env python3

import argparse

#Creating an argparse object
parser = argparse.ArgumentParser(description="this script will be used to do stuff to assignment 5")

#adding positional arguments for each of the variables below
parser.add_argument('job_name', help=("this is going to be the name of the job"), type=str)

#adding optional arguments for the rest of the 
parser.add_argument('--queue_name', help="Prints queue_name", type=str)
parser.add_argument('--number_of_nodes', help="Prints number of nodes being used")
parser.add_argument('--walltime', help="Prints the wall time of the code")
parser.add_argument('--number_of_processors', help="Prints the number of processors being used")

#setting up args to be parsed
args = parser.parse_args()

# print bash header
print('#!/bin/bash')

print()

print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition' ,args.queue_name)
print('#SBATCH --nodes=' + str(args.number_of_nodes))
print('#SBATCH --tasks-per-node=' + str(args.number_of_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o %j.out')
print('#SBATCH -e %j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=email')

# cd $SLURM_SUBMIT_DIR

# job command here
#put directory and a $ here

