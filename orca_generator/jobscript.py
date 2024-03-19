from abc import ABC, abstractmethod


class Jobscript(ABC):
    """Abstract class for ORCA jobscript."""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> str:
        """Return the ORCA jobscript string."""
        pass


class PBS_Jobscript(Jobscript):
    def __call__(self, name: str, queue: str, *args, **kwargs) -> str:
        """
        Generates a Portable Batch System (PBS) job script string. It is intended to serve as a template for further customization.
        """
        return f"""\
#!/bin/bash
#PBS -V
#PBS -N {name}
#PBS -q {queue}
#PBS -l nodes=1:ppn=4

cd $PBS_O_WORKDIR

export PATH=/home/$USER/bin:$PATH
export HOSTS_FILE=$PBS_NODEFILE

echo -e "+++ GENERAL JOB RUN INFORMATION +++\n" >> run.info
echo -e "  EXECUTED ON THE FOLLOWING NODES" >> run.info
cat $HOSTS_FILE >> run.info
"""  # TODO: enter your workflow ...


class SLURM_Jobscript(Jobscript):
    def __call__(self, name: str, partition: str, account: str, *args, **kwargs) -> str:
        """
        Generates a Simple Linux Utility for Resource Management (SLURM) job script string. It is intended to serve as a template for further customization.
        """
        return f"""\
#!/bin/bash
#SBATCH --job-name={name}
#SBATCH --partition={partition}
#SBATCH --account={account}
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --output=orca_job.out
#SBATCH --error=orca_job.err

# use directory where the script is submitted
WORK_DIR=$SLURM_SUBMIT_DIR

# set stack size to unlimited
ulimit -s unlimited

echo -e "+++ GENERAL JOB RUN INFORMATION +++\n"
echo -e "  TEMPORARY DIRECTORY\n$TMPDIR\n"
echo -e "  EXECUTED ON THE FOLLOWING NODES"
scontrol show hostname $HOSTS_FILE
"""  # TODO: enter your workflow ...
