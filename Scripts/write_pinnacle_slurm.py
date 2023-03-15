#! /usr/bin/env python3

job_name = "JobName"
queue_name = "queue"
number_of_nodes = "number of nodes"
walltime = "time to run"
number_of_processors = "number of processors"


print('#SBATCH --job-name=',job_name)
print('#SBATCH --partition',queue_name)
print('#SBATCH --nodes=',number_of_nodes)
print('#SBATCH --tasks-per-node=',number_of_processors)
print('#SBATCH --time=',walltime)
print('#SBATCH -o %j.out')
print('#SBATCH -e %j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=email')

# cd $SLURM_SUBMIT_DIR


