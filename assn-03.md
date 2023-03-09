*Questions*
1. My run time was 00:00:04
2. The closes match in the database is Arabidopsis
3. 

cd watermelon_files

cd mt_genomes

rsync -rz mt_genomes cgw028@hpc-portal2.hpc.uark.edu:/storage/cgw028/

ssh cgw028@hpc-portal2.hpc.uark.edu

module avail

cd storage/cgw028/mt_genomes

nano assign3.slurm

in the nano, I loaded a blast module, added Cat* .fasta > genomes.fas, and then added the two commands provided in the assignment PDF

sbatch assign3.slurm

exit

rsync -rvz cgw028@hpc-portal2.hpc.uark.edu:/storage/cgw028/mt_genomes .